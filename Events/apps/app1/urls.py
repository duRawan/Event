from django.urls import path, include 
from . import views

urlpatterns = [
path('', views.index),
path('admindashboard', views.AdminDash),
path('Event/<int:id>', views.showEvent),
path('editProcess/<int:id>', views.editProcess),
path('editEvent/<int:id>', views.editEvent),
path('delete/<int:id>', views.deleteEvent),
path('login',views.login),
path('register',views.register),
path('loginPage',views.loginPage),
path('registerPage',views.registerPage),
#/////////////// for testing page
path('Login',views.Login),
]