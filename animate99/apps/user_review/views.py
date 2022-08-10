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

class LibraryListView(View):
    def get(self, request, pk, *args, **kwargs):
        animations = Animation.objects.all().order_by('created_on')  

        user = CustomUser.objects.get(pk=pk)     
        context = {
            'animations': animations,
            'user':user,
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

# class SettingsView(View):
#     def get(self,request, pk, *args, **kwargs):
#         user = CustomUser.objects.get(pk=request.user.id)
#         # form = UserUpdateForm()
#         # context = {
#         #     'user':user,
#         #     'form':form
#         # }

#         return render(request, 'user_review/settings.html')
    
    # def put(self, request, pk, *args, **kwargs):
    #     user = CustomUser.objects.get(pk=request.user.id)
    #     form = UserUpdateForm(request.PUT)

    #     if form.is_valid():
    #         form.save()
    #         return redirect('settings/<int:pk>')
            
    #     context = {
    #         'user':user,
    #         'form':form,
    #     }
        
    #     return render(request, 'user_review/settings.html', context)
        
        
# import generic UpdateView

  

  
class ProfileEditView(UpdateView):
    # specify the model you want to use
    model = CustomUser
    template_name='user_review/settings.html'
    # specify the fields
    fields = [
        "name",
        "twitter_url",
        "github_url",
        "image"
    ]
    success_url ="/"    
# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)  # request.FILES is show the selected image or file


    
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

