from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView

from .serializers import ExerciseSerializer

from .models import Exercise

from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['Exercise'],

    request = ExerciseSerializer,

    responses = {200:ExerciseSerializer},

)
class ExerciseListView(ListAPIView):
    queryset = Exercise.objects.all()

    serializer_class = ExerciseSerializer



extend_schema(
    tags = ['Exercise'],

    request = ExerciseSerializer,

    responses = {200:ExerciseSerializer},

)
class ExerciseCreateView(CreateAPIView):
    queryset = Exercise.objects.all()

    serializer_class = ExerciseSerializer

class ExerciseDeleteView(DestroyAPIView):
    queryset = Exercise.objects.all()

    serializer_class = ExerciseSerializer

    lookup_field = 'id'