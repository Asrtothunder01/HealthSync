from django.urls import path

from .views import FitnessListView,FitnessCreateView

urlpatterns = [
    path('v1/',FitnessListView.as_view(),name = 'fitness'),

    path('v2/',FitnessCreateView.as_view(),name = 'fitness')
]