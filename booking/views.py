from django.shortcuts import render
from django.views import generic
from .models import Reservation
from .forms import ReservationForm
# from django.http import HttpResponse


# Create your views here.
# def my_booking(request):
#     return HttpResponse("Hello, this is the booking page!")


def create_reservation(request):
    form = ReservationForm()
    return render(
        request,
        'booking/reservation_form.html',
        {
            "form": form,
        },
    )

# def delete_reservation(request):
#     return

# def display_homepage(request):
#     return

class BookingList(generic.ListView):
    queryset = Reservation.objects.all().order_by('date', 'time')
    # template_name = "reservation_list.html"