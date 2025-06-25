from . import views
from django.urls import path

urlpatterns = [
    path('', views.display_homepage, name='homepage'),
    path('book/', views.create_reservation, name='create_reservation'),
    path('my_booking/', views.BookingList.as_view(), name='my_booking'),
]