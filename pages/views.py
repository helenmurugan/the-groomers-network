from django.shortcuts import render
from django.views import generic, View


def landing_page(request):
    """
    Render the landing page
    """
    return render(request, "landing_page.html")


def Error404(request, exception):
    """
    Render 404 error page
    """
    return render(request, "404.html", status=404)
