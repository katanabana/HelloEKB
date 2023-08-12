from django.urls import path
from .views import *

urlpatterns = [
    path('', events, name='events')

]
"""path('<pk:event_pk>', EventDetail.as_view(), name='event-detail')"""