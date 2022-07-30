from django.urls import path
from .views import download_page

urlpatterns = [
     path('download/', download_page, name='download' )
]
