from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Reservation, Table


# Register your models here.
@admin.register(Table)
class TableAdmin(SummernoteModelAdmin):
    """
    Adds additional admin panel functionality for tables through summernote.
    """
    list_display = ('table_id', 'capacity')
    search_fields = ['table_id', 'capacity']
    list_filter = ('table_id', 'capacity')


@admin.register(Reservation)
class BookingAdmin(SummernoteModelAdmin):
    """
    Adds additional admin panel functionality for bookings through summernote.
    """
    list_display = ('guest', 'table', 'time', 'date', 'duration')
    search_fields = ['guest', 'table']
    list_filter = ('guest', 'table', 'date')
    summernote_fields = ('special_reqs',)
