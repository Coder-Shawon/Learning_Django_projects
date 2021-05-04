from django.urls import path, include
from .import views

app_name = 'Myalbum'

urlpatterns = [
    path('', views.myalbum, name='Myalbum')
]