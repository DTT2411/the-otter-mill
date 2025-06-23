from . import views
from django.urls import path

urlpatterns = [
    path('my_booking/', views.BookingList.as_view(), name='my_booking'),
]