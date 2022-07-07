from unicodedata import name
from .import views 
from django.urls import path

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('about/', views.about, name = 'about-appfarm'),
    path('contacto/',views.contacto, name = 'appfarm-contacto')
]
