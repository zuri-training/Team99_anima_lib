from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'main/home.html',)

def documentation (request):
    return render(request, 'main/documentation.html',)

def download (request):
    return render(request, 'main/download.html',)

def login (request):
    return render(request, 'accounts/login.html',)

def register (request):
    return render(request, 'accounts/register.html',)

def support (request):
    return render(request, 'main/support.html',)
