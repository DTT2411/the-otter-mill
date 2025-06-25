from django.shortcuts import render
from django.views import generic
from .models import Reservation
from .forms import ReservationForm
# from django.http import HttpResponse


# Create your views here.
# def my_booking(request):
#     return HttpResponse("Hello, this is the booking page!")


def create_reservation(request):
    from .models import Table, Reservation
    from django.db.models import Q
    error_message = None
    assigned_table = None

    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.guest = request.user
            # Find available tables with enough capacity
            number_of_guests = reservation.number_of_guests
            date = reservation.date
            time = reservation.time
            duration = reservation.duration

            # Get tables with enough capacity
            suitable_tables = Table.objects.filter(capacity__gte=number_of_guests).order_by('capacity')
            # Exclude tables already booked for the requested date and time
            booked_tables = Reservation.objects.filter(date=date, time=time).values_list('table_id', flat=True)
            available_tables = suitable_tables.exclude(id__in=booked_tables)

            if available_tables.exists():
                assigned_table = available_tables.first()
                reservation.table = assigned_table
                reservation.save()
            else:
                error_message = "No available table for the selected date, time, and number of guests."
        else:
            error_message = "Invalid form submission."
    else:
        form = ReservationForm()
    return render(request, 'booking/reservation_form.html', {"form": form, "error_message": error_message, "assigned_table": assigned_table})
# def delete_reservation(request):
#     return

def display_homepage(request):
    return render(request, 'booking/homepage.html')

# def display_homepage(request):
#     return

class BookingList(generic.ListView):
    queryset = Reservation.objects.all().order_by('date', 'time')
    # template_name = "reservation_list.html"