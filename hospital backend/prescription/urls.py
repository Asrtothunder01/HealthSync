from django.urls import path

from .views import PrescriptionListView,PrescriptionCreateView

urlpatterns =[
    path('v1/',PrescriptionListView.as_view(),name = 'patient'),

    path('v2/',PrescriptionCreateView.as_view(),name = 'patient'),
]