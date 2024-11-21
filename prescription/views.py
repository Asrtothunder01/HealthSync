from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import PrescriptionSerializer

from .models import Prescription
from drf_spectacular.utils import extend_schema


extend_schema(
    tags = ['Prescription'],

    request = PrescriptionSerializer,

    responses = {200:PrescriptionSerializer},

)
class PrescriptionListView(ListAPIView):
    queryset = Prescription.objects.all()

    serializer_class = PrescriptionSerializer


extend_schema(
    tags = ['Prescription'],

    request = PrescriptionSerializer,

    responses = {201:PrescriptionSerializer},

)
class PrescriptionCreateView(CreateAPIView):
    queryset = Prescription.objects.all()

    serializer_class = PrescriptionSerializer

