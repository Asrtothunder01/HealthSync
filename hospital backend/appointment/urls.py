from django.urls import path

from .views import AppointmentListView,AppointmentCreateView

urlpatterns =[
    path('v1/',AppointmentListView.as_view(),name = 'patient'),

    path('v2/',AppointmentCreateView.as_view(),name = 'patient'),
]