from django.shortcuts import render
from django.views import generic, View


def landing_page(request):
    """
    Landing page
    """
    return render(request, "landing_page.html")


# following code was taken from Kim Borgstroem's PP4
# https://github.com/KimBergstroem/PP4
def Error403(request, exception=None):
    """
    Custom 403 page
    """
    return render(request, "403.html", status=403)


def Error404(request, exception=None):
    """
    Custom 404 page
    """
    return render(request, "404.html", status=404)


def Error405(request, exception=None):
    """
    Custom 405 page
    """
    return render(request, "405.html", status=405)


def Error500(request):
    """
    Custom 500 page
    """
    return render(request, "500.html", status=500)
