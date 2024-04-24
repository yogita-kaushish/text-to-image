from django.contrib import admin
from text_to_image.models import Requests, Prompts


# Register your models here.
admin.site.register(Requests)
admin.site.register(Prompts)
