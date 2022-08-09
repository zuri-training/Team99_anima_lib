from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Animation
from django.views import View
from django.http import HttpResponse
from apps.accounts.models import CustomUser
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

class SettingsView(View):
    def get(self,request, pk, *args, **kwargs):
        user = CustomUser.objects.get(pk=request.user.id)

        context = {
            'user':user
        }

        return render(request, 'user_review/settings.html', context)



    
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
        
            
            
        next = request.POST.get('next', "/dashboard/library")
        return  HttpResponseRedirect(next)
        # return render(request, 'library')
        

def likes (request):
    return render(request, 'user_review/likes.html',)

