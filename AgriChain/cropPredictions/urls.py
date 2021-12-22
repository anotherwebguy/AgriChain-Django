from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crops/<str:name>/' , views.crop_profile , name = 'crop_profile'),
]