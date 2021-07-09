from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showIndex, name='home'),
    path('trainningdetails', views.showTrainningDetails, name='trainningdetails'),
    path('contactus', views.contactus, name='contactus'),
    path('feedback', views.feedback, name='feedback'),
    path('delete/<int:id>', views.delete, name="delete"),
]
