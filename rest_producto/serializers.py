from rest_framework import fields, serializers
from core.models import Producto, Marca

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = '__all__'
    def to_representation(self, instance):
        rep = super(ProductoSerializer, self).to_representation(instance)
        rep['marca_nombre'] = instance.marca.nombre
        return rep

class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'
    