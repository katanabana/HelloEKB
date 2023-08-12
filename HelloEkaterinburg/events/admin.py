from django.contrib import admin
from .models import Event


"""class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}"""


admin.site.register(Event)
