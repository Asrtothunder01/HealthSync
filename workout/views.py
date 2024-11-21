from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import WorkoutSerializer,RoutineSerializer,SessionSerializer

from .models import WorkoutRoutine,WorkoutExercise,WorkoutSession

from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['WorkRoutine'],

    request = RoutineSerializer,

    responses = {200:RoutineSerializer},
)
class RoutineListView(ListAPIView):
    queryset = WorkoutRoutine.objects.all()

    serializer_class = RoutineSerializer


extend_schema(
    tags = ['workRountine'],

    request = RoutineSerializer,

    responses = {200:RoutineSerializer},

)
class RoutineCreateView(CreateAPIView):
    queryset = WorkoutRoutine.objects.all()

    serializer_class = RoutineSerializer



extend_schema(
    tags = ['WorkExercise'],

    request = WorkoutSerializer,

    responses = {200:WorkoutSerializer},
)

class WorkoutListView(ListAPIView):
    queryset = WorkoutExercise.objects.all()

    serializer_class = WorkoutSerializer

extend_schema(
    tags = ['workExercise'],

    request = WorkoutSerializer,

    responses = {200:WorkoutSerializer},
)
class WorkoutCreateView(CreateAPIView):

    queryset = WorkoutExercise.objects.all()

    serializer_class = WorkoutSerializer



extend_schema(
    tags = ['WorkSession'],

    request = SessionSerializer,

    responses = {200:SessionSerializer},
)
class SessionListView(ListAPIView):
    queryset = WorkoutSession.objects.all()

    serializer_class = SessionSerializer


extend_schema(
    tags = ['workSession'],

    request = SessionSerializer,

    responses = {200:SessionSerializer},
)
class SessionCreateView(CreateAPIView):
    queryset = WorkoutSession.objects.all()

    serializer_class = SessionSerializer