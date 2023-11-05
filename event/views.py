from django.shortcuts import render
from django.views import generic
from .models import Event

class PostList(generic.ListView):
    model = Event
    queryset = Post.objects.order_by("-created_on")
    template_name = "event.html"
    paginate_by = 6

