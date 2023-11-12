from django.shortcuts import render
from django.views import generic, View

def landing_page(request):
    """
    Render the landing_page template.
    """
    return render(request, "landing_page.html")