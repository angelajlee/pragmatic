from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    return render(request, 'account-app/helloworld.html')