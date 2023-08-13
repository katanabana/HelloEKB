import django_filters
from django_filters import CharFilter

from .models import Event


class EventFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Event
        fields = ["category"]
