from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ListRooms.as_view(), name = "list_rooms"),
    path('list_rooms/', views.ListRooms.as_view(), name = "list_rooms"),
    path('reservations/<int:room_id>/', views.ListRoomReservations.as_view(), name = "list_room_reservations"),
    path('reservations/update/<int:pk>/', views.UpdateReservation.as_view(), name = "update_room_reservations"),
    # path('reservations/create/', views.CreateRoomReservations.as_view(), name = "create_room_reservations")
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
