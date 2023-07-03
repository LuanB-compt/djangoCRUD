from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.create),
    path('read/', views.read),
    path('update/', views.update),
    path('delete/', views.delete)
]
