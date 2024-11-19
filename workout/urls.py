from django.urls import path

from .views import RoutineCreateView,RoutineListView,ExerciseCreateView,ExerciseListView,SessionListView,SessionCreateView

urlpatterns =[
    path('v1/',RoutineListView.as_view(),name = 'patient'),

    path('v2/',RoutineCreateView.as_view(),name = 'patient'),
    
    path('exercise/v1/',ExerciseListView.as_view(),name= 'Exercise'),

    path('exercise/v2/',ExerciseCreateView.as_view(),name = 'exercise'),

    path('session/v1/',SessionListView.as_view(),name = 'session'),

    path('session/v2/',SessionCreateView.as_view(),name = 'session'),

]