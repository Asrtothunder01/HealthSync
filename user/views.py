from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import FitnessSerializer

from .models import FitnessUser

from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['Fitness'],

    request = FitnessSerializer,

    responses = {200:FitnessSerializer},
)
class FitnessListView(ListAPIView):
    queryset = FitnessUser.objects.all()

    serializer_class = FitnessSerializer

extend_schema(
    tags = ['workExercise'],

    request = FitnessUser,

    responses = {200:FitnessSerializer},
)
class FitnessCreateView(CreateAPIView):
    queryset = FitnessUser.objects.all()

    serializer_class = FitnessSerializer