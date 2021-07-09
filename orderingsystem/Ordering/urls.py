from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.showOrder, name="order"),
      path('orderdetails', views.showDetails, name="orderdetails"),
       path('orderdetails/<int:id>', views.edit, name="edit"),
        path('fulldetails/<int:id>', views.fulldetails, name="fulldetails"),
        path('update/<int:id>', views.update, name="update"),
        path('delete/<int:id>', views.delete, name="delete"),
        path('deletecompleted/<int:id>', views.deletecompleted, name="deletecompleted"),
       path('completedorder', views.compOrder, name="completedorder"),
       path('paypal/<int:id>', views.paypal, name="paypal"),
     
     path('reports', views.searchHandle, name="reports"),
     path('report', views.searchHandle1, name="reports"),
     
    
     path('userorders', views.showUserORder, name="userorders"),
     path('cart', views.cart, name="cart"),
    
     path('userordersdelete/<int:id>', views.userordersdelete, name="userordersdelete"),
     path('generateinvoice', views.invoice, name="invoice"),
    
]