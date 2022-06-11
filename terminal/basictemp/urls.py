 
 
from django.urls import path,include
from . import views

urlpatterns = [
 
    path('basic/', views.basictemp ,name="basictemp"),
]
