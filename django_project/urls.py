"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Web_1.views import index, about, contact, form, edit_form, delete, upload_file, input_num, form_up_img, delete_img

urlpatterns = [
	path('', index, name='index'),
	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('my_form/', form, name='form'),
	path('my_form/edit_form/<int:id>/', edit_form, name='edit_form'),
	path('my_form/delete/<int:id>/', delete),
	path('form_up_img/', form_up_img, name='form_up_img'),
	path('form_up_img/delete_img/<int:id>/', delete_img),
	path('upload/', upload_file, name='upload_file'),
	path('input/', input_num, name= 'input_num'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


