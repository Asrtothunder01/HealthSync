from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import MealSerializer

from .models import Meal

from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['Meal'],

    request = MealSerializer,

    responses = {200:MealSerializer},

)
class MealListView(ListAPIView):
    queryset = Meal.objects.all()

    serializer_class = MealSerializer


extend_schema(
    tags = ['Meal'],

    request = MealSerializer,

    responses = {201:MealSerializer},

)
class MealCreateView(CreateAPIView):
    queryset =  Meal.objects.all()

    serializer_class = MealSerializer