from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('email')
                messages.success(request, user + ' ' +  'account created, kindly login .'  )

               
                
                
                       
                
                return redirect('accounts:login')

            
        context= {
            'form':form,
        }
        return render(request, "accounts/register.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('library')
            else:
                messages.info(request, 'Email OR password is incorrect')           
        context= {}
        return render(request, "accounts/login.html", context )
    


# @login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('accounts:login')


def forgot_view(request):
    return render (request,'accounts/reset_page1.html')

def reset_view(request):
    return render (request,'accounts/reset_page2.html')
