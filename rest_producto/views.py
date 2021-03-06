from django.shortcuts import render
from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from core.models import Marca
from .serializers import ProductoSerializer
from .serializers import MarcaSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_productos(request):

    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_marcas(request):
    if request.method == 'GET':
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarcaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_productos(request, codigo):
    try:
        producto = Producto.objects.get(codigo = codigo)
    except:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        producto.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_marcas(request, id):
    try:
        marca = Marca.objects.get(id = id)
    except:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MarcaSerializer(marca, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        marca.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)