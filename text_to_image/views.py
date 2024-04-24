from datetime import datetime
from text_to_image.models import Requests, Prompts
from django.shortcuts import render
from django.forms import model_to_dict
from django.http import JsonResponse
from text_to_image.tasks import generate_image_task
import os
import threading
import uuid

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
tmp_dir = os.path.join(BASE_DIR, 'data')


# Create your views here.
def generate_images(request):
    print(f"--------------generate_images-----------------")
    print(f"request.body:{request.POST}")

    request_body = request.POST

    if len(request_body) > 0:
        request_id = save_request_info('Pending', request_body)
        print(f"A request with {request_id.id} has been accepted.")
    context = {
        'get_request_info': get_requests()
    }
    return render(request, 'home.html', context)


def save_request_info(status, prompts):
    intercepted_at = datetime.now()
    result = Requests.objects.create(intercepted_at=intercepted_at, status=status)
    thread = threading.Thread(target=save_prompt_info(prompts, result))
    thread.start()
    return result


def save_prompt_info(prompts, request_info):
    for prompt in prompts.keys():
        file_name = str(uuid.uuid4())+".webp"
        if prompt.startswith('prompt') and prompts[prompt]:
            print(f"prompts:{prompts[prompt]}")
            print(f"file_name:{file_name}")
            response = generate_image_task(prompts[prompt], file_name)
            if response == 200:
               Prompts.objects.create(content=prompt, status=response, response_url=file_name, request=request_info)
    return


def get_requests():
    request_info = {}
    index = 0
    q_request_all = Requests.objects.all()
    if len(q_request_all) > 0:
        for request in q_request_all:
            index = index + 1
            request = model_to_dict(request)
            request_info[index] = {}
            request_info[index]['request_id'] = request['id']
            request_info[index]['intercepted_at'] = request['intercepted_at']
            request_info[index]['status'] = request['status']
    return request_info


def get_request_prompts(request, request_id):
    index = 0
    request = Requests.objects.get(id = request_id)
    q_prompt_all = Prompts.objects.filter(request=request)
    results = []
    if len(q_prompt_all) > 0:
        for prompt in q_prompt_all:
            index = index + 1
            prompt = model_to_dict(prompt)
            results.append(prompt)
    return JsonResponse(results, safe=False)