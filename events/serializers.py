from rest_framework import serializers
from django.utils.timezone import now  
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'location', 'capacity', 'created_date']

    def validate_date_time(self, value):
        # Ensure that the event date and time are not in the past
        if value < now():
            raise serializers.ValidationError("Event date and time cannot be in the past.")
        return value


