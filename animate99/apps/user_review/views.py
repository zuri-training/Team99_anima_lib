from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Animation
from django.views import View
from django.http import HttpResponse
from apps.accounts.models import CustomUser
from django.views import View
# from .forms import EditProfileForm
from .forms import UserUpdateForm
from django.views.generic.edit import UpdateView
# from django.contrib.auth.forms import UserChangeForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class LibraryListView(View,LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        animations = Animation.objects.all().order_by('created_on')
        # is_liked = Animation.objects.filter(favourites=request.user.id)
        
        
        context = {
            'animations': animations,
            # 'is_liked': is_liked,
            
        }
        
        return render(request, 'user_review/library.html', context)
    
class LibraryDetailView(View,LoginRequiredMixin):
    def get(self, request, pk, *args, **kwargs):
        animation = Animation.objects.get(pk=pk)
        user = CustomUser.objects.get(pk=request.user.id)
        is_favourite = False
        
        if animation.favourites.filter(id=request.user.id).exists():
            animation.favourites.remove(request.user)
            is_favourite = True

        context = {
            'animation': animation,
            'is_favourite': is_favourite,
        }
        
        return render(request, 'user_review/library.html', context)
    
    

class ProfileEditView(UpdateView, LoginRequiredMixin):
    model = CustomUser
    template_name='user_review/settings.html'
    fields = ["name", "twitter_url","github_url", "image"]
    # success_url ="settings" 
    
    def get_success_url(self):
        return self.request.path



@login_required(login_url='login')    
def usageExamples (request):
    return render(request, 'user_review/usageExamples.html',)

class IsFavoriteView(View,LoginRequiredMixin):
    def post(self, request,pk, *args, **kwargs):
        animation = Animation.objects.get(pk=pk)
        is_favourite = False
        
        
        if animation.favourites.filter(id=request.user.id).exists():
            animation.favourites.remove(request.user)
            is_favourite = False
        else:
            animation.favourites.add(request.user)
            is_favourite = True
        
            
            
        next = request.POST.get('next', f"/dashboard/library/")
        return  HttpResponseRedirect(next)
    
class IsLiked(View,LoginRequiredMixin):
    def post(self, request,pk, *args, **kwargs):
        animation = Animation.objects.get(pk=pk)
        is_favourite = False
        
        link_id = request.user.id
        
        
        if animation.favourites.filter(id=request.user.id).exists():
            animation.favourites.remove(request.user)
            is_favourite = False
        else:
            animation.favourites.add(request.user)
            is_favourite = True
        
            
        next = request.POST.get('next', f"/dashboard/likes/{link_id}/")            
        # next = request.POST.get('next', f"/dashboard/likes/{link_id}/")
        return  HttpResponseRedirect(next)
        


class LikesView(View, LoginRequiredMixin):
    def get(self, request, pk, *args, **kwargs):
        user = CustomUser.objects.get(pk=pk)
        animations = Animation.objects.filter(favourites=request.user.id)
        
        context = {
            'user': user,
            'animations': animations,
        }
        
        
        return render(request, 'user_review/likes.html', context)
        
