from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import PatientSerializer

from .models import Patient
from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['Patient'],

    request = PatientSerializer,

    responses = {200:PatientSerializer},

)
class PatientListView(ListAPIView):
    queryset = Patient.objects.all()

    serializer_class = PatientSerializer

extend_schema(
    tags = ['Patient'],

    request = PatientSerializer,

    responses = {201:PatientSerializer},

)
class PatientCreateView(CreateAPIView):
    queryset = Patient.objects.all()

    serializer_class = PatientSerializer