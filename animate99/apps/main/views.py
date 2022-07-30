from django.shortcuts import render

# Create your views here.
def download_page(request):
    return render(request, "main/download.html")