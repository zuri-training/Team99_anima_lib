from django.urls import path
from .views import blog_page

app_name='blog'
urlpatterns = [
    path("", blog_page, name="index" ),
]