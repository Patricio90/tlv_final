from unicodedata import name
from .import views 
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos, name='productos'),
    path('lista', views.listar, name='lista'),
    path('productos/crear_productos', views.crear_producto, name='crear'),
    path('productos/editar_productos', views.editar_producto, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/editar/<int:id>', views.editar_producto, name='editar'),
    path('about/', views.about, name = 'about-appfarm'),
    path('contacto/',views.contacto, name = 'appfarm-contacto')

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
