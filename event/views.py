from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by("-created_on")
    template_name = "event.html"
    paginate_by = 6


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "event_detail.html",
            {
                "event": post,
                "comments": comments,
                "liked": liked
            },
        )
