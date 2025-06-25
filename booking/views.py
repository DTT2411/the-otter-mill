from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservation, Table
from .forms import ReservationForm
from datetime import datetime, timedelta
# from django.http import HttpResponse


# Create your views here.
# def my_bookings(request):
#     return HttpResponse("Hello, this is the booking page!")




@login_required
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

            # Combine date & time for calculation with timedelta
            requested_start = datetime.combine(date, time)
            # Calculates the requested end time by adding the duration to the start time
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
                    # Calculates whether there is an overlap between the requested time and existing time on the table
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


def delete_reservation(request, reservation_id):
    from django.shortcuts import get_object_or_404
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, id=reservation_id, guest=request.user)
        reservation.delete()
        messages.success(request, "Reservation deleted successfully.")
    return redirect('my_bookings')


def display_homepage(request):
    return render(request, 'booking/homepage.html')


class BookingList(generic.ListView):
    model = Reservation
    template_name = "booking/reservation_list.html"

    def get_queryset(self):
        return Reservation.objects.filter(guest=self.request.user).order_by('date', 'time')