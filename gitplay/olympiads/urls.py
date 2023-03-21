from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.list_olympiads, name='olympiads'),
    path('<int:id>/', views.show_olympiad, name='olympiad')
]