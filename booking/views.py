from django.shortcuts import render
from django.views import generic
from .models import Reservation
# from django.http import HttpResponse


# Create your views here.
# def my_booking(request):
#     return HttpResponse("Hello, this is the booking page!")

class BookingList(generic.ListView):
    # model = Reservation
    queryset = Reservation.objects.all().order_by('date', 'time')
    template_name = "reservation_list.html"