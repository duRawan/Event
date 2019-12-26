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
path('logout',views.logout),
path('loginPage',views.loginPage),
path('registerPage',views.registerPage),
path('profile',views.profile),
path('Book/<int:id>',views.bookEvent),
path('addEvent',views.addEvent),
path('profile',views.profile),
path('Book/<int:id>',views.bookEvent),
path('editProfProcess/<int:id>',views.editProfProcess),
path('editProfile/<int:id>',views.editProfile),
]