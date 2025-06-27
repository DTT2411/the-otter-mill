from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from datetime import datetime, timedelta
from .models import Reservation, Table
from .forms import ReservationForm


# If the user is not logged in, they will be redirected to the login page
@login_required
def create_reservation(request):
    """
    Creates a single instance of :model:`booking.Reservation`. Checks whether
    there is a suitable table based on time, date and number of guests.

    **Context**

    ``form``
        An instance of :form:`booking.ReservationForm`
    ``error-message``
        Error message passed if there is no table available or an invalid form
    ``assigned-table``
        The assigned table if allocation has been successful
    """
    # Initialises the variables which will be passed to the template
    error_message = None
    assigned_table = None

    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.guest = request.user
            number_of_guests = reservation.number_of_guests
            date = reservation.date
            time = reservation.time
            duration = reservation.duration
            # Combine date & time for calculation with timedelta
            requested_reservation_start = datetime.combine(date, time)
            # Calculates the requested end time by adding the duration to the
            # start time
            requested_reservation_end = requested_reservation_start + timedelta(minutes=duration)
            # "capacity__gte" finds tables with capacity >= number of guests,
            # then puts them in ascending order so the smallest suitable table
            # is checked first
            suitable_tables = Table.objects.filter(capacity__gte=number_of_guests).order_by('capacity')
            available_tables = []
            for table in suitable_tables:
                # Calculates end time for each existing reservation and check
                # for overlap with requested time
                has_overlap = False
                for existing_reservation in Reservation.objects.filter(table=table, date=date):
                    # Combines data & time into one variable for operations
                    # with timedelta
                    existing_reservation_start = datetime.combine(existing_reservation.date, existing_reservation.time)
                    existing_reservation_end = existing_reservation_start + timedelta(minutes=existing_reservation.duration)
                    # If an overlap is found, breaks out of the loop so the
                    # next table can be checked
                    if requested_reservation_start < existing_reservation_end and requested_reservation_end > existing_reservation_start:
                        has_overlap = True
                        break
                if not has_overlap:
                    available_tables.append(table)
            if available_tables:
                # Assigns the first available table based on updated details
                assigned_table = available_tables[0]
                reservation.table = assigned_table
                reservation.save()
                messages.success(request, "Reservation successful!")
                # Returns user to a blank reservation form in case they want
                # to make another reservation
                return redirect('create_reservation')
            else:
                error_message = "No available table at your selected time."
        else:
            error_message = "Invalid form submission."
    else:
        form = ReservationForm()
    return render(request, 'booking/reservation_form.html', {
        "form": form,
        "error_message": error_message,
        "assigned_table": assigned_table
    })


@login_required
def edit_reservation(request, reservation_id):
    """
    Updates a single instance of :model:`booking.Reservation`. Checks whether
    there is a suitable table based on time, date and number of guests.

    **Context**

    ``form``
        An instance of :form:`booking.ReservationForm`
    ``error-message``
        Error message passed if there is no table available or an invalid form
    ``assigned-table``
        The assigned table if allocation has been successful
    ``edit-mode``
        Populates template with existing data to facilitate editing
    """
    # Pulls the existing reservation based on its ID
    reservation = get_object_or_404(Reservation, id=reservation_id, guest=request.user)
    # Initialises the variables which will be passed to the template
    error_message = None
    assigned_table = reservation.table

    if request.method == 'POST':
        form = ReservationForm(data=request.POST, instance=reservation)
        if form.is_valid():
            updated_reservation = form.save(commit=False)
            number_of_guests = updated_reservation.number_of_guests
            date = updated_reservation.date
            time = updated_reservation.time
            duration = updated_reservation.duration
            # Combine date & time for calculation with timedelta
            requested_reservation_start = datetime.combine(date, time)
            # Calculates requested end time by adding the duration to the
            # start time
            requested_reservation_end = requested_reservation_start + timedelta(minutes=duration)
            # "capacity__gte" finds tables with capacity >= number of guests,
            # then puts them in ascending order so the smallest suitable table
            # is checked first
            suitable_tables = Table.objects.filter(capacity__gte=number_of_guests).order_by('capacity')
            available_tables = []
            for table in suitable_tables:
                # Calculates end time for each existing reservation and check
                # for overlap with requested time
                has_overlap = False
                for existing_reservation in Reservation.objects.filter(table=table, date=date).exclude(id=reservation.id):
                    # Combines data & time into one variable for operations
                    # with timedelta
                    existing_reservation_start = datetime.combine(existing_reservation.date, existing_reservation.time)
                    existing_reservation_end = existing_reservation_start + timedelta(minutes=existing_reservation.duration)
                    if requested_reservation_start < existing_reservation_end and requested_reservation_end > existing_reservation_start:
                        # If an overlap is found, breaks out of the loop so
                        # the next table can be checked
                        has_overlap = True
                        break
                if not has_overlap:
                    available_tables.append(table)
            if available_tables:
                # Assigns the first available table based on updated details
                assigned_table = available_tables[0]
                updated_reservation.table = assigned_table
                updated_reservation.save()
                messages.success(request, "Reservation updated successfully!")
                # Redirects to My Bookings screen so that they can see updates
                return redirect('my_bookings')
            else:
                error_message = "No available table at your selected time."
        else:
            error_message = "Invalid form submission."
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'booking/reservation_form.html', {
        "form": form,
        "error_message": error_message,
        "assigned_table": assigned_table,
        "edit_mode": True
    })


def delete_reservation(request, reservation_id):
    """
    Deletes an individual booking.

    **Context**

    ``reservation``
        An instance of :model:`booking.Reservation
    """
    if request.method == 'POST':
        reservation = get_object_or_404(
            Reservation, id=reservation_id, guest=request.user)
        reservation.delete()
        messages.success(request, "Reservation deleted successfully.")
    # The "My Bookings" screen is refreshed after deletion
    return redirect('my_bookings')


def display_homepage(request):
    """
    Renders the homepage template.
    """
    return render(request, 'booking/homepage.html')


class BookingList(generic.ListView):
    """
    Returns a list of bookings, restricted to only those made by the currently
    logged-in user.
    """
    model = Reservation
    template_name = "booking/reservation_list.html"

    def get_queryset(self):
        return Reservation.objects.filter(guest=self.request.user).order_by(
            'date', 'time')
