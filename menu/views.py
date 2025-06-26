from django.shortcuts import render

# Create your views here.
def display_menu(request):
    return render(request, 'menu/menu_list.html')


