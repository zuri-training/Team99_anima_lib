from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Animation
from django.views import View
# Create your views here.

class LibraryListView(View):
    def get(self, request, *args, **kwargs):
        animations = Animation.objects.all().order_by('created_on')
        

        context = {
            'animations': animations,
        }
        
        return render(request, 'user_review/library.html', context)
    
class LibraryDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        animation = Animation.objects.get(pk=pk)
        is_favourite = False
        
        if animation.favourites.filter(id=request.user.id).exists():
            animation.favourites.remove(request.user)
            is_favourite = True

        context = {
            'animation': animation,
            'is_favourite': is_favourite,
        }
        
        return render(request, 'user_review/library.html', context)
# def library (request):
    
#     return render(request, 'user_review/library.html',)

def settings (request):
    return render(request, 'user_review/settings.html',)
    
def usageExamples (request):
    return render(request, 'user_review/usageExamples.html',)

class IsFavoriteView(View):
    def post(self, request,pk, *args, **kwargs):
        animation = Animation.objects.get(pk=pk)
        is_favourite = False
        
        if animation.favourites.filter(id=request.user.id).exists():
            animation.favourites.remove(request.user)
            is_favourite = False
        else:
            animation.favourites.add(request.user)
            is_favourite = True
        
            
        # animations = Animation.objects.all()
            
            
        
        # for favourite in animation.favourites.all():
        #     if favourite == request.user:
        #         is_favourite = True
        #         break
            
        # if not is_favourite:
        #     animation.favourites.add(request.user)
        
        # if is_favourite:
        #     animation.favourites.remove(request.user)
            
        next = request.POST.get('next', "/dashboard/library")
        return  HttpResponseRedirect(next)
        # return render(request, 'library')
        

def likes (request):
    return render(request, 'user_review/likes.html',)

