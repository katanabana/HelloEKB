from django.contrib import admin
from .models import Event, EventFromPublic

"""class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}"""


admin.site.register(Event)
admin.site.register(EventFromPublic)
