from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appBook.urls')),
    path('', include('appAuthentication.urls')),
    path('', include('appProfile.urls')),
]
