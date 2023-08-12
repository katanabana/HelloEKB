from django.urls import path
from .views import *

urlpatterns = [
    path('events/', events, name='events')

]
"""path('<pk:event_pk>', EventDetail.as_view(), name='event-detail')"""