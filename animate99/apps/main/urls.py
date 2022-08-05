from django.urls import path
from .views import home, documentation,download,register,login,support

urlpatterns = [
     path("", home, name='home' ),
     path("documentation", documentation, name='documentation' ),
     path("download", download, name='download' ),
     path("login", login, name='login' ),
     path("register", register, name='register' ),
     path("support", support, name='support' ),


]
