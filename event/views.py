from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event


class EventList(generic.ListView):
    """
    View for displaying a list of events
    """
    model = Event
    queryset = Event.objects.order_by("-created_on")
    template_name = "event.html"
    paginate_by = 6


class EventDetail(View):
    """
    View for displaying a selected event.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Display selected event
        """
        queryset = Event.objects
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "event_detail.html",
            {
                "event": post,
                "liked": liked
            },
        )


class EventLike(View):
    """
    View to toggle likes on events
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Toggles likes on event
        """
        event = get_object_or_404(Event, slug=slug)
        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))
