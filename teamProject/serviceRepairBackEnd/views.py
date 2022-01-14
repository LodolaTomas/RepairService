from django.shortcuts import render, HttpResponse
from rest_framework import serializers
from .models import Cliente
from .serializers import ClienteSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def cliente_list(request):
    
    #get all clients
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializers = ClienteSerializer(clientes, many=True)
        return JsonResponse(serializers.data, safe=False,status=200)
    elif request.method == 'POST':
        print(request.POST)
        data =  JSONParser().parse(request) #z b  rer no se que es esto pero me tiraba error.
        serializers = ClienteSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
    return JsonResponse(serializers.errors, status=400)
