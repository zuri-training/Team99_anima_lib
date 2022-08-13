from django.urls import path
from .views import home, documentation,download, support,download_file

urlpatterns = [
     path("", home, name='home' ),
     path("documentation", documentation, name='documentation' ),
     path("download", download, name='download' ),
     path("support", support, name='support' ),
     path('downloadfile', download_file, name="download-file" )

]
