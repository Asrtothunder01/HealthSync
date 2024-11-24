from django.urls import path

from .views import MedicalListView,MedicalCreateView

urlpatterns =[
    path('v1/',MedicalListView.as_view(),name = 'medical'),

    path('v2/',MedicalCreateView.as_view(),name = 'medical'),
]