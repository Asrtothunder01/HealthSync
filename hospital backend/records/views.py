from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import MedicalSerializer

from .models import  MedicalRecord
from drf_spectacular.utils import extend_schema


extend_schema(
    tags = ['Medical Record'],

    request = MedicalSerializer,

    responses = {200:MedicalSerializer},

)
class MedicalListView(ListAPIView):
    queryset = MedicalRecord.objects.all()

    serializer_class = MedicalSerializer

extend_schema(
    tags = ['Medical Record'],

    request = MedicalSerializer,

    responses = {201: MedicalSerializer},

)
class MedicalCreateView(CreateAPIView):
    queryset = MedicalRecord.objects.all()

    serializer_class = MedicalSerializer