from django.shortcuts import render

from .vk_events import get_events
from .filters import EventFilter
from .models import Event, EventFromPublic


def events(request):
    events = Event.objects.all()
    filter = EventFilter(request.GET, queryset=events)
    events = filter.qs

    for description in get_events():
        event = EventFromPublic(description=description)
        event.save()

    context = {"events": events,
               "filter": filter}

    return render(request, "events/events.html", context)


"""class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    pk = 'id'
    context_object_name = 'event'
"""
