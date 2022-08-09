from django.urls import path
from .views import library,usageExamples, likes, SettingsView

urlpatterns = [
     path("library", library, name='library' ),
     path("settings/<int:pk>/", SettingsView.as_view(), name='settings'),
     path("usageexamples", usageExamples, name='usageexamples' ),
     path("likes", likes, name='likes' )

]
