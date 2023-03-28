from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime



def current_year():
    return datetime.date.today().year

def max_year(value):
    return MaxValueValidator(current_year())(value)


class Year(models.Model):
    year = models.PositiveBigIntegerField(
        default=current_year(),
        validators=[MinValueValidator(2000), max_year],
        unique=True
    )

    def __str__(self) -> str:
        return str(self.year)

    class Meta:
        ordering = ['year']



class Period(models.Model):
    start_year = models.ForeignKey(Year, on_delete=models.PROTECT, related_name='start_years')
    end_year = models.ForeignKey(Year, on_delete=models.PROTECT, related_name='end_years')

    def __str__(self) -> str:
        if self.start_year == self.end_year:
            return str(self.start_year)
        return f'{str(self.start_year)}/{str(self.end_year)}'
    
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['start_year', 'end_year'],
                name='Unique period',
            )
        ),

        ordering = ['start_year', 'end_year']