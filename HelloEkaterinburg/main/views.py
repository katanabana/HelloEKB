from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView


def main(request):
    context = {}
    return render(request, "main/main.html", context)
