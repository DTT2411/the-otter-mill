from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MenuItem


# Register your models here.
@admin.register(MenuItem)
class MenuAdmin(SummernoteModelAdmin):
    """
    Adds additional admin panel functionality for menu items through
    summernote.
    """
    list_display = ('name', 'type', 'price')
    search_fields = ['name']
    list_filter = ('type',)
