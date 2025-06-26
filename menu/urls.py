from django.urls import path 
from . import views

urlpatterns = [
    path('', views.display_menu, name='display_menu'),
]