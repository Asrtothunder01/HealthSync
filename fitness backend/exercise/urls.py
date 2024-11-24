from django.urls import path

from .views import ExerciseListView,ExerciseCreateView,ExerciseDeleteView

urlpatterns = [

    path('v1/',ExerciseListView.as_view(),name = 'exercise'),
    
    path('v2/',ExerciseCreateView.as_view(),name = 'exercise'),

    path('<int:id>/v3/',ExerciseDeleteView.as_view(),name = 'exercise'),
]