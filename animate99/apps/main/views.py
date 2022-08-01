from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'main/home.html',)

def documentation (request):
    return render(request, 'main/documentation.html',)
