from django.urls import path
from .views import LibraryListView,usageExamples, ProfileEditView, IsFavoriteView, LikesView
# SettingsView, ,
# app_name = 'dashboard'
urlpatterns = [
     path("library/<int:pk>/", LibraryListView.as_view(), name='library' ),
     path("settings/<pk>/", ProfileEditView.as_view(), name='settings'),
     path("usageexamples", usageExamples, name='usageexamples' ),
     path("likes/<int:pk>/", LikesView.as_view(), name='likes' ),
     path("isfavourite/<int:pk>/", IsFavoriteView.as_view(), name='favourite')
]
