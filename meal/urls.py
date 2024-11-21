from django.urls import path

from .views import MealListView,MealCreateView

urlpatterns = [

    path('v1/',MealListView.as_view(),name = 'meal'),
    
    path('v2/',MealCreateView.as_view(),name = 'meal'),
]