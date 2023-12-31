from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.create),
    path('read/', views.read),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete)
]
