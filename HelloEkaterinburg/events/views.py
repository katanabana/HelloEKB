from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from .filters import EventFilter
from .models import Event


def events(request):
    events = Event.objects.all()
    filter = EventFilter(request.GET, queryset=events)
    events = filter.qs

    context = {"events": events,
               "filter": filter}

    return render(request, "events/events.html", context)


"""class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    pk = 'id'
    context_object_name = 'event'
"""


