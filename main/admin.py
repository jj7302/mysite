from django.contrib import admin
from .models import Voulunteer_Event, Profile

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    fields = ["user",
              "event_name",
              "hours",
    ]

class ProfileAdmin(admin.ModelAdmin):
    fields = ["user",
              "organization",
              "access",
    ]

admin.site.register(Voulunteer_Event, EventAdmin)
admin.site.register(Profile, ProfileAdmin)
