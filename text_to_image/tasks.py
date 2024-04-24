import os
import requests
from celery import shared_task
from blue_butterfly.settings import STABILITY_API_BASE_URL, STABILITY_AI_API_KEY, MEDIA_ROOT
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMG_DATA_DIR = os.path.join(BASE_DIR, "media")

@shared_task
def generate_image_task(prompt, file_name):
    print(f"------------generate_image_task---------------")

    headers = {"authorization": f"Bearer {STABILITY_AI_API_KEY}", "accept": "image/*"}

    payload = {
        "prompt": prompt,
        "output_format": "webp",
    }

    files = {"none": ""}

    response = requests.post(
        url=f"{STABILITY_API_BASE_URL}/v2beta/stable-image/generate/core",
        headers=headers,
        files=files,
        data=payload,
    )

    print(f"generate_image_task request sent")

    # save response to file
    if response.status_code == 200:
        save_resp_to_file(response, file_name)
        return response.status_code
    else:
        print(f"generate_image_task response{Exception(str(response.json()))}")
        return response.status_code


def save_resp_to_file(response, file_name):
    print(f"--------------save_resp_to_file---------------------")
    file_path = os.path.join(MEDIA_ROOT, f"{file_name}.webp")
    # Open the file using the constructed file path
    with open(file_path, "wb") as file:
        # Write the image contents to the file
        file.write(response.content)
    return
