from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def blog_page(request):
    return HttpResponse("Hello, I am Brandon Stark")