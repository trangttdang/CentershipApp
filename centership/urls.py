# django_project/urls.py
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # new
]
    
=======
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('profiles.urls')),
]
>>>>>>> develop
