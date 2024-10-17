from django.urls import path
from . import views as ak_views

urlpatterns = [
    path("", ak_views.home, name="home"),
    path('location/', ak_views.location, name='location')
]
