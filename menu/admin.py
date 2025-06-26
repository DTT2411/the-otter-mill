from django.contrib import admin
from .models import MenuItem
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(MenuItem)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('name', 'type', 'price')
    search_fields = ['name']
    list_filter = ('type',)