from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer, BookingDetailSerializer, UpdateBookingSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class UpdateBookingView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = UpdateBookingSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class CancelBookingView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = FlightListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
