from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.list_olympiads, name='olympiads'),
    path('exercises/', views.list_exercises, name='exercises'),
    path('exercises/<slug:slug>', views.show_exercise, name='exercise'),
    path('<slug:slug>/', views.show_olympiad, name='olympiad'),
    path('create/exercise-type', views.create_exercise_type, name='create_exercise_type')
]