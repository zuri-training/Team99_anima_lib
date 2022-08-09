from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, PasswordInput,TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email': EmailInput(attrs={
                'class': "email",
                'id': "email",
                # 'style': 'max-width: 300px;'
                'placeholder': 'Name'
                }),
            'password1': PasswordInput(attrs={
                'class': "password", 
                'id': "password1",
                'style': 'background-color: white;',
                'placeholder': "Enter password"
                }),
            'password2': PasswordInput(attrs={
                'class': "password", 
                'id': "password",
                # 'style': 'max-width: 300px;',
                'placeholder': "Confirm password"
                })
        }