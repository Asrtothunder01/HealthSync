from django.urls import path

from .views import DietListView,DietCreateView

urlpatterns = [

    path('v1/',DietListView.as_view(),name = 'Diet'),
    
    path('v2/',DietCreateView.as_view(),name = 'diet'),
]