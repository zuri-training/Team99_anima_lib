from django.shortcuts import render
from django.http import HttpResponse
from apps.accounts.models import CustomUser
from django.views import View

# Create your views here.
def library (request):
    return render(request, 'user_review/library.html',)


class SettingsView(View):
    def get(self,request, pk, *args, **kwargs):
        user = CustomUser.objects.get(pk=request.user.id)

        context = {
            'user':user
        }

        return render(request, 'user_review/settings.html', context)


# def settings (request):
#     photo = CustomUser.objects.all()
#     # adding context 
#     ctx = {'photo':photo}
#     return render(request, 'user_review/settings.html', ctx)
    
def usageExamples (request):
    return render(request, 'user_review/usageExamples.html',)

def likes (request):
    return render(request, 'user_review/likes.html',)

