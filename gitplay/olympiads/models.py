from django.db import models
from core import constants
from core.models import Period

class Olympiad(models.Model):
    name = models.CharField(max_length=256)
    level = models.CharField(max_length=3, choices=constants.OLYMPIAD_LEVELS, default='VOS')
    slug = models.SlugField(default='vos')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['id']

    

class ExerciseType(models.Model):
    type = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.type

    class Meta:
        ordering = ['type']


class OlympiadExercise(models.Model):
    type = models.ForeignKey(ExerciseType, on_delete=models.PROTECT, related_name='olympic_exercises', default=None)
    code = models.CharField(max_length=256, primary_key=True)
    olympiad = models.ForeignKey(Olympiad, on_delete=models.PROTECT, related_name='olympic_exercises')
    task_description = models.TextField()
    contents = models.TextField()
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='olympic_exercises')
    slug = models.SlugField()


    def __str__(self) -> str:
        return f'{str(self.type)} {str(self.code)}'

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['type', 'code'],
                name='Unique task code',
            )
        ),

        ordering = ['type', 'code']