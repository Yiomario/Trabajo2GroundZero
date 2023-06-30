from django.contrib import admin
from .models import Arte, Producto, Formulario
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "stock", "arte"]
    list_editable = ["precio", "stock", "arte"]
    search_fields = ["nombre"]
    list_filter = ["arte"]
    list_per_page = 5

class FormularioAdmin(admin.ModelAdmin):
    list_display = ["rut", "correo", "tipo_consulta"]
    search_fields = ["rut"]
    list_filter = ["tipo_consulta"]
    list_per_page = 5

admin.site.register(Arte)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Formulario, FormularioAdmin)