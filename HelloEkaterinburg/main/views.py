from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from events.models import Event


def main(request):
    sport = Event.get_last_from("Sport")
    culture = Event.get_last_from("Culture")
    education = Event.get_last_from("Education")
    hobby = Event.get_last_from("Hobby")
    context = {"sport": sport, "culture": culture, "education": education, "hobby": hobby}
    print(context)
    return render(request, "main/main.html", context)
