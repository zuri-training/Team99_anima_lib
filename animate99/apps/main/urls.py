from django.urls import path
from .views import home
from .views import documentation

urlpatterns = [
     path("", home, name='home' ),
     path("documentation", documentation, name='documentation' ),

]
