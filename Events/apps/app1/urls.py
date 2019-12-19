from django.urls import path, include 
from . import views

urlpatterns = [
path('', views.index),
path('admindashboard', views.AdminDash),
path('Event/<int:id>', views.showEvent)
]