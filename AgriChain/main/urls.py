from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('contact.html',views.contact, name='contact'),
    path('blog.html',views.blog, name='blog'),
    path('services.html',views.services, name='services'),
    path('gallery.html',views.gallery, name='gallery'),
    path('typo.html',views.typo, name='typo')
]