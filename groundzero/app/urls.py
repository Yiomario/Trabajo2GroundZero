from django.urls import path
from .views import index, formulario, inicio, imagen1, imagen2, imagen3,\
    imagen4, imagen5, imagen6, imagen7, imagen8, agregar_producto,\
     listar_productos, modificar_producto,eliminar_producto, galeria, servicio, registrar

urlpatterns = [
    path('', index, name="index"),
    path('formulario/', formulario, name="formulario"),
    path('inicio/', inicio, name="inicio"),
    path('imagen1/', imagen1, name="imagen1"),
    path('imagen2/', imagen2, name="imagen2"),
    path('imagen3/', imagen3, name="imagen3"),
    path('imagen4/', imagen4, name="imagen4"),
    path('imagen5/', imagen5, name="imagen5"),
    path('imagen6/', imagen6, name="imagen6"),
    path('imagen7/', imagen7, name="imagen7"),
    path('imagen8/', imagen8, name="imagen8"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registrar/', registrar, name="registrar"),
    path('galeria/', galeria, name="galeria"),
    path('servicio/', servicio, name="servicio"),
    
]
    
