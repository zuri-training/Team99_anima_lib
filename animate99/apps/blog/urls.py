from . import views
from django.urls import path
from apps.blog.views import front_page, post_detail


#My imports
urlpatterns = [
    path("", front_page, name="front_page.html" ),
    path('<slug:slug>/', post_detail, name='post_detail'),
    #path('', views.PostList.as_view(), name='post_detail'), <<using generic views>>
]