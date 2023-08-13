from django.urls import path

from .views import *

urlpatterns = [
    path('events/', events, name='events')

]