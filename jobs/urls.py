from django.urls import path
from .views import CreateJobView,ListJobsView,JobDetailsView,get_all_locations
app_name='jobs'
urlpatterns=[
    path('create/',CreateJobView.as_view()),
    path('',ListJobsView.as_view(),name='list'),
    path('<slug:slug>/',JobDetailsView.as_view()),
    path('city/locations/',get_all_locations)
]
