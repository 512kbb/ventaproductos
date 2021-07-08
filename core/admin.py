from django.contrib import admin
from .models import Producto, Marca
# Register your models here.

class detalleMarca(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_per_page = 20
    list_display = ["nombre", "descripcion"]
    list_filter = ["nombre", "descripcion"]

class detalleProducto(admin.ModelAdmin):
    list_display = ["modelo", "marca", "precio", "color"]
    list_filter = ["modelo", "marca", "precio", "color"]
    list_editable = ["precio"]
    list_per_page = 20
    search_fields = ["modelo"]


admin.site.register(Marca, detalleMarca)
admin.site.register(Producto, detalleProducto)



