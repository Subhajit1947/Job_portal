from django.urls import path
from .views import registerUser,logout_view
urlpatterns=[
    path('register/',registerUser,name='register'),
    path('logout/',logout_view,name='logout_view'),
    
]
