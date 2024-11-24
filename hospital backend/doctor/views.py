from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import DoctorSerializer

from .models import Doctor

from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['Meal'],

    request = DoctorSerializer,

    responses = {200:DoctorSerializer},

)
class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer


class DoctorCreateView(CreateAPIView):
    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer