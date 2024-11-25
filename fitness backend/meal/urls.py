from django.urls import path

from .views import MealListView,MealCreateView,design

urlpatterns = [
    path('',design,name='base'),

    path('v1/',MealListView.as_view(),name = 'meal'),
    
    path('v2/',MealCreateView.as_view(),name = 'meal'),
]