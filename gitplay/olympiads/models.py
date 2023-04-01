from django.db import models
from core import constants
from core.models import Period


class Level(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.level

    class Meta:
        ordering = ['id']


class Tag(models.Model):
    tag = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.tag

    class Meta:
        ordering = ['tag']


class Olympiad(models.Model):
    name = models.CharField(max_length=256)
    level = models.ForeignKey(Level, on_delete=models.PROTECT, related_name='olympiads')
    slug = models.SlugField()
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='olympiads')

    def __str__(self) -> str:
        return f'{self.name} {str(self.period)}'
    
    class Meta:
        ordering = ['-period', 'id']

    

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
    tags = models.ManyToManyField(Tag, related_name='olympiads')


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