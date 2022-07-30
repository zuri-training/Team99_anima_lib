from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
# Create your views here.

def register_view(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            
            
            return redirect('login')
        
    context= {
        'form':form,
    }
    return render(request, "accounts/register.html", context )


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('download')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
        
        
    context= {}
    return render(request, "accounts/login.html", context )

def logout_user(request):
    logout(request)
    return redirect('accounts:login')
