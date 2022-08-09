from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

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
        send_mail("User Support Enquiry", message, 'animate99team99@gmail.com', [email], fail_silently=False)
            
    return render(request, 'main/support.html')
