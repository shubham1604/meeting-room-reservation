from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MeetingRoom, Reservation
from .serializers import MeetingRoomSerializer, ReservationSerializer
from rest_framework import generics
from rest_framework import permissions
from core.permissions import IsOwnerOrReadOnly


class ListRooms(generics.ListCreateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ListRoomReservations(generics.ListCreateAPIView):

    serializer_class = ReservationSerializer
    lookup_field = 'room_id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self,**kwargs):
        if self.request.method == "GET":
            return Reservation.objects.filter(room_id = self.kwargs.get('room_id'), status=Reservation.RESERVED)

        return super().get_queryset(**kwargs)

    def perform_create(self, serializer):
        serializer.save(organiser=self.request.user)


class UpdateReservation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
