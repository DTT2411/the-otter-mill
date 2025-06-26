from django.shortcuts import render
from django.views import generic
from .models import MenuItem

# Create your views here.
# def display_menu(request):
#     return render(request, 'menu/menu_list.html')


class MenuList(generic.ListView):
    """
    Renders a list of all MenuItem objects to the menu_list.html template.
    """
    model = MenuItem
    template_name = "menu/menu_list.html"

    # Returns a list of all menu items
    def get_queryset(self):
        return MenuItem.objects.all().order_by('type', 'name')