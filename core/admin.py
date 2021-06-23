from django.contrib import admin
from .models import MeetingRoom, Reservation, MeetingInvitees


admin.site.register(MeetingRoom)
admin.site.register(Reservation)
admin.site.register(MeetingInvitees)
