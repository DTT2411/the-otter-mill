from . import views
from django.urls import path

urlpatterns = [
    # path('booking/', views.Booking.as_view(), name='booking'),
    path('book/', views.create_reservation, name='create_reservation'),
    path('my_booking/', views.BookingList.as_view(), name='my_booking'),
]