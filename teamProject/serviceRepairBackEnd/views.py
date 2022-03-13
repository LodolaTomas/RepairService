from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ClienteSerializer, TecnicoSerializer # para los metodos post necesito importar el serializer
from .models import Cliente, Tecnico

# Login y Logout Imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



@csrf_exempt
def client_api(request):
    """
    List all clients, or create a new client.
    """
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        cliente = ClienteSerializer(data=data)
        if cliente.is_valid():
            cliente.save()
            return JsonResponse(cliente.data, status=201)
        return JsonResponse(cliente.errors, status=400)

    elif request.method == 'DELETE':
        cliente = Cliente.objects.all()
        cliente.delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def client_detail (request, cuil):
    """
    Retrieve, update or delete a client.
    """
    try:
        cliente = Cliente.objects.get(cuil=cuil)
    except Cliente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(cliente, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cliente.delete()
        return HttpResponse(status=204)

@csrf_exempt
def tecnico_api(request):
    """
    tecnico
    """
    if request.method == 'GET':
        tecnico = Tecnico.objects.all()
        serializer = TecnicoSerializer(tecnico, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        tecnico = TecnicoSerializer(data=data)
        if tecnico.is_valid():
            tecnico.save()
            return JsonResponse(tecnico.data, status=201)
        return JsonResponse(tecnico.errors, status=400)

    elif request.method == 'DELETE':
        tecnico = Tecnico.objects.all()
        tecnico.delete()
        return HttpResponse(status=204)





# CRUD de Room necesito tus conocimientos en React.js
# Realizar el Hashing de password para cada user.
# Que cada user tenga un rango inicial cuando se lo crea.
# User Login Sigo necesitando React Info
#
#def loginInfo(request):
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')

#        try:
#            user = User.objects.get(username=username)
#        except:
#            messages.error(request,'user does not exist')
#        
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('home')
#        else:
#            messages.error(request, 'Username or password does not exist')
#    context = {}
#    return "hola"

#def logoutUser(request):
#    logout(request)
#    return redirect('home')