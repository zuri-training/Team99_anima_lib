from django.urls import path
from .views import LibraryListView, settings,usageExamples, likes, IsFavoriteView

urlpatterns = [
     path("library", LibraryListView.as_view(), name='library' ),
     path("settings", settings, name='settings'),
     path("usageexamples", usageExamples, name='usageexamples' ),
     path("likes", likes, name='likes' ),
     path("isfavourite/<int:pk>/", IsFavoriteView.as_view(), name='favourite')
]
