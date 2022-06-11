 
 
from django.urls import path,include
from . import views

urlpatterns = [
 
    path('ceditor/', views.ceditor ,name="ceditor"),
    path('save/', views.save_data, name='save'),
]
