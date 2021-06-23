from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MeetingRoom(models.Model):
    room_number = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE, default=1)

    def __str__(self):
        return f"Room No. {self.room_number}"

class Reservation(models.Model):

    RESERVED = "RESERVED"
    CANCELLED = "CANCELLED"

    RESERVATION_STATUS_CHOICES = [
    (RESERVED, "Reserved"),
    (CANCELLED, "Cancelled")
    ]

    title = models.CharField(max_length=100, default = 'Title')
    meeting_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    reserved_from = models.DateTimeField()
    reserved_to = models.DateTimeField()
    room = models.ForeignKey(MeetingRoom, on_delete = models.CASCADE)
    organiser = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length=20, choices = RESERVATION_STATUS_CHOICES, default = RESERVED)
    invitees = models.ManyToManyField(User, related_name="reservation_invitees", through="MeetingInvitees")

    def __str__(self):
        return f"{self.title}"

class MeetingInvitees(models.Model):

    GOING = "GOING"
    NOT_GOING = "NOT GOING"
    MAY_BE = "MAY BE"

    RESPONSE_CHOICES = [
    (GOING,"Going"),
    (NOT_GOING,"Not Going"),
    (MAY_BE,"May be"),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    meeting = models.ForeignKey(Reservation, on_delete = models.CASCADE)
    response = models.CharField(max_length=20, choices = RESPONSE_CHOICES)

    def __str__(self):
        return "Faang"

    # class Meta:
    #     unique_together = ['user', 'meeting']
