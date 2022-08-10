from django.urls import include, path
from .views import register_view, login_view, logout_user, reset_view, forgot_view

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name="login" ),
    path('logout/', logout_user, name="logout" ),
    path('forgotpassword/', forgot_view, name="forgotpassword" ),
    path('resetpassword/', reset_view, name="resetpassword" ),
    
]