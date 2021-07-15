"""weddingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from jean import views
from django.conf.urls import include


urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^jean/', include('jean.urls')),
    path('admin/', admin.site.urls),
    path('rsvp/',views.rsvp,name='rsvp'),
    path('details/',views.details,name='honeymoon'),
    path('honeymoon/',views.honeymoon,name='honeymoon'),
    path('photos/',views.photos,name='photos'),
]
