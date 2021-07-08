from django.urls import path
from rest_producto.views import lista_productos, lista_marcas, detalle_productos, detalle_marcas


urlpatterns = [
    path('listado-productos/', lista_productos, name="listado-productos"),
    path('listado-marcas/', lista_marcas, name="listado-marcas"),

    path('detalle-productos/<codigo>', detalle_productos, name="detalle-productos"),
    path('detalle-marcas/<nombre>', detalle_marcas, name="detalle-marcas"),
]