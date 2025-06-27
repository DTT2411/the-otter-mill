from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_homepage, name='homepage'),
    path('book/', views.create_reservation, name='create_reservation'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation,
         name='delete_reservation'),
    path('my_bookings/', views.BookingList.as_view(), name='my_bookings'),
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation,
         name='edit_reservation'),
]
