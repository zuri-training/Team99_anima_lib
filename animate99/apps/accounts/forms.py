from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, PasswordInput,TextInput
from allauth.socialaccount.forms import SignupForm
from django.forms import ValidationError

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
        


class CustomSignupForm(SignupForm):
     def raise_duplicate_email_error(self):
         raise ValidationError("שם משתמש כבר קיים עם כתובת אימייל")