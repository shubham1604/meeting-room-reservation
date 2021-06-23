from rest_framework import serializers
from .models import MeetingRoom, Reservation, MeetingInvitees
from django.contrib.auth.models import User
from django.db.models import Q, F


class MeetingRoomSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = 'created_by.username')

    class Meta:
        model = MeetingRoom
        fields = ["room_number", 'created_by']


class ReservationSerializer(serializers.ModelSerializer):
    organiser = serializers.ReadOnlyField(source='organiser.username')
    invitees = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    def validate(self, data):
        reserved_from = data.get('reserved_from')
        reserved_to = data.get('reserved_to')
        room = data.get('room')

        if (reserved_from > reserved_to):
            raise serializers.ValidationError("Start time can't be after or equal to end time")

        reservation_exists = Reservation.objects.filter(
        Q(reserved_from__lt=reserved_from, reserved_to__gt=reserved_from)|
        Q(reserved_from__lt=reserved_to, reserved_to__gt=reserved_to)|
        Q(reserved_from=reserved_from)|
        Q(reserved_to=reserved_to),
        room=room,
        status=Reservation.RESERVED
        ).exists()

        if reservation_exists:
            raise serializers.ValidationError(f"The slot you asked for room {room.room_number} is not available. Kindly book a different slot or a different room")

        return data

    class Meta:
        model = Reservation
        fields = "__all__"
        
