from django.forms import ModelForm
from apps.accounts.models import CustomUser
from django.contrib.auth.forms import UserChangeForm

class UserUpdateForm(UserChangeForm):
    # name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    # email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # twitter_url = forms.URLField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Twitter Profile Link'}))
    # github_url = forms.URLField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Github Profile Link'}))
    class Meta:
        model = CustomUser
        fields = ['name', 'twitter_url', 'github_url']
        # fields= "__all__"
        
class EditProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = (
                'name',
                'twitter_url',
                'github_url'
                )