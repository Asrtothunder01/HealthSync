from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import AppointmentSerializer

from .models import Appointment
from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['Appointment'],

    request = AppointmentSerializer,

    responses = {200:AppointmentSerializer},

)
class AppointmentListView(ListAPIView):
    queryset = Appointment.objects.all()

    serializer_class = AppointmentSerializer

extend_schema(
    tags = ['Appoitment'],

    request = AppointmentSerializer,

    responses = {201:AppointmentSerializer},

)
class AppointmentCreateView(CreateAPIView):
    queryset = Appointment.objects.all()

    serializer_class = AppointmentSerializer