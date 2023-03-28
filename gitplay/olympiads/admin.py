from django.contrib import admin
from . import models



admin.site.register(models.Olympiad)
admin.site.register(models.ExerciseType)
admin.site.register(models.OlympiadExercise)
admin.site.register(models.Level)
admin.site.register(models.Tag)