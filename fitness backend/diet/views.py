from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import DietSerializer

from .models import DietPlan
from drf_spectacular.utils import extend_schema

extend_schema(
    tags = ['Diet'],

    request = DietSerializer,

    responses = {200:DietSerializer},

)
class DietListView(ListAPIView):
    queryset = DietPlan.objects.all()

    serializer_class = DietSerializer


extend_schema(
    tags = ['Diet'],

    request = DietSerializer,

    responses = {201:DietSerializer},

)
class DietCreateView(CreateAPIView):
    queryset = DietPlan.objects.all()

    serializer_class = DietSerializer