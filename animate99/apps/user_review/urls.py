from django.urls import path
from .views import library, settings,usageExamples, likes

urlpatterns = [
     path("library", library, name='library' ),
     path("settings", settings, name='settings'),
     path("usageexamples", usageExamples, name='usageexamples' ),
     path("likes", likes, name='likes' )

]
