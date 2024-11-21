from django.urls import path

from .views import DoctorListView,DoctorCreateView

urlpatterns =[
    path('v1/',DoctorListView.as_view(),name = 'patient'),

    path('v2/',DoctorCreateView.as_view(),name = 'patient'),
]