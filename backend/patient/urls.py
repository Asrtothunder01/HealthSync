from django.urls import path

from .views import PatientListView,PatientCreateView

urlpatterns =[
    path('v1/',PatientListView.as_view(),name = 'patient'),

    path('v2/',PatientCreateView.as_view(),name = 'patient'),
]