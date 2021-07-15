from django.conf.urls import url
from django.urls import path
from jean import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('rsvp/',views.rsvp,name='rsvp'),
    path('details/',views.details,name='honeymoon'),
    path('honeymoon/',views.honeymoon,name='honeymoon'),
    path('photos/',views.photos,name='photos'),
]
