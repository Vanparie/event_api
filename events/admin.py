from django.contrib import admin
from .models import Event, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'date_time', 'location', 'organizer', 'capacity', 'created_date')
    # Fields to make searchable in the admin panel
    search_fields = ('title', 'location', 'organizer__username')
    # Fields to use for filtering in the admin panel
    list_filter = ('date_time', 'location')
    # Fields to display as read-only
    readonly_fields = ('created_date',)

    # Customize the admin form for events
    fieldsets = (
        ("Event Details", {
            "fields": ("title", "description", "date_time", "location", "organizer", "capacity"),
        }),
        ("Meta Information", {
            "fields": ("created_date",),
        }),
    )


    # Optional Enhancements
    ordering = ('date_time',)  # Default ordering by event date
    list_per_page = 20         # Display 20 events per page in the admin panel