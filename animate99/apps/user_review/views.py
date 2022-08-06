from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def library (request):
    return render(request, 'user_review/library.html',)

def settings (request):
    return render(request, 'user_review/settings.html',)
    
def usageExamples (request):
    return render(request, 'user_review/usageExamples.html',)

def likes (request):
    return render(request, 'user_review/likes.html',)

