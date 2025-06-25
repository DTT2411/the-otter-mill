from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservation, Table
from .forms import ReservationForm
from datetime import datetime, timedelta


# Create your views here.

# If the user is not logged in, they will be redirected to the login page
@login_required
def create_reservation(request):

    # Initialises the error and table variables which will be passed to the template
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
            requested_reservation_start = datetime.combine(date, time)
            # Calculates the requested end time by adding the duration to the start time
            requested_reservation_end = requested_reservation_start + timedelta(minutes=duration)

            # "capacity__gte" finds tables with capacity >= number of guests,
            # then puts them in ascending order so the smallest suitable table
            # is checked first
            suitable_tables = Table.objects.filter(capacity__gte=number_of_guests).order_by('capacity')
            available_tables = []
            for table in suitable_tables:
                # Calculates end time for each existing reservation and check for overlap with requested time
                has_overlap = False
                for existing_reservation in Reservation.objects.filter(table=table, date=date):
                    # Combines data & time into one variable for operations with timedelta
                    existing_reservation_start = datetime.combine(existing_reservation.date, existing_reservation.time)
                    existing_end = existing_reservation_start + timedelta(minutes=existing_reservation.duration)
                    # If an overlap is found, breaks out of the loop so the next table can be checked
                    if requested_reservation_start < existing_end and requested_reservation_end > existing_reservation_start:
                        has_overlap = True
                        break
                if not has_overlap:
                    available_tables.append(table)

            if available_tables:
                # Assigns the first available table as this will be the smallest which is suitable for the current booking
                assigned_table = available_tables[0]
                reservation.table = assigned_table
                reservation.save()
                messages.success(request, "Reservation successful!")
                # Returns user to a blank reservation form in case they want to make another reservation
                return redirect('create_reservation')
            else:
                error_message = "No available table at your selected time."
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
    # The "My Bookings" screen is refreshed after deletion
    return redirect('my_bookings')


def display_homepage(request):
    return render(request, 'booking/homepage.html')


class BookingList(generic.ListView):
    model = Reservation
    template_name = "booking/reservation_list.html"

    # Returns a list of bookings, restricted to only those made by the currently logged-in user
    def get_queryset(self):
        return Reservation.objects.filter(guest=self.request.user).order_by('date', 'time')