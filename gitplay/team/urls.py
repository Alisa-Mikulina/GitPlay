from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_team, name='team'),
    path('<str:name>/', views.team_member, name='team_member')
]