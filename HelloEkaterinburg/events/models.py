import os.path

from django.db import models
from django.db.models import DateTimeField, CharField


def get_img_path(instance, filename):
    extension = filename.split('.')[-1]
    return os.path.join('event_images', f'{instance.pk}.{extension}')


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
    place = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
