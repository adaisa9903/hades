from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def myfirtsview(request):
    data = {
        'name': 'Ada'
    }
    return JsonResponse(data)

def  mysecondview(request):
    return HttpResponse('Hola mundo')