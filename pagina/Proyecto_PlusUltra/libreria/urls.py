from xml.dom.minidom import Document
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros', views.libros, name='libros'),
    path('mangas', views.mangas, name='mangas'),
    path('comics', views.comics, name='comics'),
    path('libros/crear_libro', views.crear_libro, name='crear_libro'),
     path('libros/crear_manga', views.crear_manga, name='crear_manga'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)