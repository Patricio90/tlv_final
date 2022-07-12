from unicodedata import name
from .import views
from user import views as user_views 
from django.urls import path


urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('about/', views.about, name = 'about-appfarm'),
    path('contacto/',views.contacto, name = 'appfarm-contacto'),
    path('registro/',user_views.registro, name='registro'),
    path('catalogo/',user_views.catalogo, name ='catalogo')
]
