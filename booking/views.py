from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Reservation, Table
from .forms import ReservationForm
from datetime import datetime, timedelta
# from django.http import HttpResponse


# Create your views here.
# def my_bookings(request):
#     return HttpResponse("Hello, this is the booking page!")


def create_reservation(request):

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

            # Calculate requested start and end datetime
            requested_start = datetime.combine(date, time)
            requested_end = requested_start + timedelta(minutes=duration)

            # Get tables with enough capacity
            suitable_tables = Table.objects.filter(capacity__gte=number_of_guests).order_by('capacity')
            available_tables = []
            for table in suitable_tables:
                # Calculate end time for each existing reservation and check for overlap
                has_overlap = False
                for existing in Reservation.objects.filter(table=table, date=date):
                    existing_start = datetime.combine(existing.date, existing.time)
                    existing_end = existing_start + timedelta(minutes=existing.duration)
                    # Overlap if requested_start < existing_end and requested_end > existing_start
                    if requested_start < existing_end and requested_end > existing_start:
                        has_overlap = True
                        break
                if not has_overlap:
                    available_tables.append(table)

            if available_tables:
                assigned_table = available_tables[0]
                reservation.table = assigned_table
                reservation.save()
                messages.success(request, "Reservation successful!")
                return redirect('create_reservation')
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