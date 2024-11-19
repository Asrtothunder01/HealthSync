from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import ExerciseSerializer,RoutineSerializer,SessionSerializer

from .models import WorkoutRoutine,WorkoutExercise,WorkoutSession

class RoutineListView(ListAPIView):
    queryset = WorkoutRoutine.objects.all()

    serializer_class = RoutineSerializer


class RoutineCreateView(CreateAPIView):
    queryset = WorkoutRoutine.objects.all()

    serializer_class = RoutineSerializer


class ExerciseListView(ListAPIView):
    queryset = WorkoutExercise.objects.all()

    serializer_class = ExerciseSerializer

class ExerciseCreateView(CreateAPIView):
    queryset = WorkoutExercise.objects.all()

    serializer_class = ExerciseSerializer

class SessionListView(ListAPIView):
    queryset = WorkoutSession.objects.all()

    serializer_class = SessionSerializer

class SessionCreateView(CreateAPIView):
    queryset = WorkoutSession.objects.all()

    serializer_class = SessionSerializer