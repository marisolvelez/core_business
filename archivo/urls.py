from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.uploadFile, name='upload_file'),
    path('archivo_subido/', views.archivo_subido, name='archivo_subido')
]
