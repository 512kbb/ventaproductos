from rest_framework import fields, serializers
from core.models import Producto, Marca

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'modelo', 'precio', 'color', 'talla', 'marca']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombre', 'descripcion']