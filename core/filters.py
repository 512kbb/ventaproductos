from django.db.models import fields
import django_filters
from django_filters import filters

from .models import *


class productoFiltro(django_filters.FilterSet):
    codigo = filters.CharFilter()
    class Meta:
        model = Producto
        fields = {
            'codigo': ['exact', 'icontains'],
            'modelo': ['exact', 'contains'],
            'precio': ['exact', 'contains'],
            'marca__nombre': ['exact', 'contains'],
        }
      

