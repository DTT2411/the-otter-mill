from django.contrib import admin
from .models import Reservation, Table
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('guest', 'table', 'time', 'date', 'duration')
    search_fields = ['guest', 'table']
    list_filter = ('guest', 'table', 'date')
    summernote_fields = ('special_reqs',)

# Register your models here.
# admin.site.register(Reservation)
admin.site.register(Table)
