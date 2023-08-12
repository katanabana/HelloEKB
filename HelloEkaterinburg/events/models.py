from django.db import models
from django.db.models import DateTimeField, CharField


class Event(models.Model):
    CATEGORY = [
    ["Sport", "Sport"],
    ["Culture", "Culture"],
    ["Education", "Education"],
    ["Hobby", "Hobby"]
    ]
    time_create = DateTimeField("Date of creation", auto_now_add=True, null=True, blank=True)
    time_update = DateTimeField("Date of update", auto_now=True, null=True, blank=True)
    # fields:
    name = CharField("Name", max_length=255, null=True, blank=True)
    category = models.CharField("Category", max_length=255, null=True, blank=True, choices=CATEGORY)
    description = models.CharField("Description", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
