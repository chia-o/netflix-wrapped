"""
URL configuration for wrapped_site project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.wrapped_app.urls')),
]
