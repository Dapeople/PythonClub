from django.contrib import admin
from .models import Meeting, MeetingMinutes, Resource, Event, User


admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(Event)
admin.site.register(User)
#admin.site.Register()
#admin.site.Register()

# Register your models here.
