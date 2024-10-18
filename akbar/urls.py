from django.urls import path
from . import views as ak_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ak_views.home, name="home"),
    path('location/', ak_views.location, name='location'),
    path('logout/', ak_views.logout_view, name='logout'),
]
