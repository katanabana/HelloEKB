import datetime
import os.path

from django.db import models
from django.db.models import DateTimeField, CharField


def get_img_path(instance, filename):
    extension = filename.split('.')[-1]
    if instance.pk:
        file_id = instance.pk
    else:
        file_id = len(Event.objects.all())
    return os.path.join('event_images', f'{file_id}.{extension}')


class Event(models.Model):
    CATEGORY = [
        ["Sport", "Спорт"],
        ["Culture", "Культура"],
        ["Education", "Образование"],
        ["Hobby", "Хобби"]
    ]
    time_create = DateTimeField("Date of creation", auto_now_add=True, null=True, blank=True)
    time_update = DateTimeField("Date of update", auto_now=True, null=True, blank=True)
    # fields:
    name = CharField("Name", max_length=255, null=True, blank=True)
    category = models.CharField("Category", max_length=255, null=True, blank=True, choices=CATEGORY)
    description = models.TextField("Description", max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=get_img_path, null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    map_code = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_datetime(self):
        start = self.start_datetime
        end = self.end_datetime

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    @classmethod
    def get_last_from(cls, category):
        events = [i for i in cls.objects.all() if i.category == category]
        if events:
            print(sorted(events, key=lambda event: event.start_datetime)[0])
            return sorted(events, key=lambda event: event.start_datetime)[0]
