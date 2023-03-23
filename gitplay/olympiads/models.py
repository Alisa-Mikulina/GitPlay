from django.db import models
from core import constants

class Olympiad(models.Model):
    name = models.CharField(max_length=256)
    level = models.CharField(max_length=3, choices=constants.OLYMPIAD_LEVELS, default='VOS')
    slug = models.SlugField(default='vos')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['id']