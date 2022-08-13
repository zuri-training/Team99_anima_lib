from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
import mimetypes
import os
from pathlib import Path
# Import HttpResponse module
from django.http.response import HttpResponse



BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def home (request):
    return render(request, 'main/home.html',)

@login_required(login_url='login')
def documentation (request):
    return render(request, 'main/documentation.html',)

@login_required(login_url='login')
def download (request):
    return render(request, 'main/download.html',)

def download_file(request):
    obj = BASE_DIR
    filename = 'script.js'
    response = FileResponse(open(filename, 'rb'))
    return response

def support (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        
        body = {
            'name' : name,
            'email': email,
            'textarea': textarea,
        }
        
        # message = "\n".join(body.values())
        
        message = f"{body['name']} \n {body['email']} \n{body['textarea']}"   
        send_mail("User Support Enquiry", message, 'animate99team99@gmail.com', ['animate99team99@gmail.com'], fail_silently=False)
            
    return render(request, 'main/support.html')
