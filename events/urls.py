from django.urls import path
from .views import EventListCreateView, EventDetailView

urlpatterns = [
    path('api/events/', EventListCreateView.as_view(), name='event_list_create'),
    path('api/events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]
