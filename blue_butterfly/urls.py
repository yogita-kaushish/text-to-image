from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from text_to_image.views import generate_images,get_request_prompts
from django.views.static import serve
from blue_butterfly.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generate_images),
    path('generate_images', generate_images),
    path('requests/<str:request_id>/', get_request_prompts)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)