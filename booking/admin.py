from django.contrib import admin
from .models import Reservation, Table
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Table)
class TableAdmin(SummernoteModelAdmin):

    list_display = ('table_id', 'capacity')
    search_fields = ['table_id', 'capacity']
    list_filter = ('table_id', 'capacity')

@admin.register(Reservation)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('guest', 'table', 'time', 'date', 'duration')
    search_fields = ['guest', 'table']
    list_filter = ('guest', 'table', 'date')
    summernote_fields = ('special_reqs',)


