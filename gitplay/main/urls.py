from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.main, name='GitPlay'),
    path('olympiads/', views.list_olympiads, name='olympiads'),
    path('team/', views.list_team, name='team'),
]