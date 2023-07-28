"""
URL configuration for SteamAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('countries/', include('countries.urls')),
    path('cities/', include('cities.urls')),
    path('system_requirements/', include('system_requirements.urls')),
    path('publishers/', include('publishers.urls')),
    path('developers/', include('developers.urls')),
    path('games/', include('games.urls')),
    path('categories/', include('categories.urls')),
    path('users/', include('users.urls')),
    path('users_libraries/', include('users_libraries.urls')),
    path('user_desired_games/', include('users_desired_games.urls')),
    path('reviews/', include('reviews.urls'))
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
