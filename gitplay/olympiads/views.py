from django.shortcuts import render
from olympiads.models import Olympiad, OlympiadExercise
from django.core.exceptions import ObjectDoesNotExist
from core.models import Period, Year
import datetime


def define_current_period():
    current_month = datetime.date.today().month
    current_year = datetime.date.today().year

    if current_month > 9:
        start_year = Year.objects.get(year=current_year)
        end_year = Year.objects.get(year=current_year + 1)
    else:
        start_year = Year.objects.get(year=current_year - 1)
        end_year = Year.objects.get(year=current_year)
    
    current_period = Period.objects.get(start_year=start_year, end_year=end_year)

    return current_period




def list_olympiads(request):

    current_period = define_current_period()

    all_olympiads = Olympiad.objects.filter(period=current_period)

    context = {
        'olympiads': all_olympiads
    }

    return render(request, 'olympiads.html', context=context)




def show_olympiad(request, slug):

    current_period = define_current_period()

    try:
        olympiad = Olympiad.objects.get(slug=slug, period=current_period)
        print(olympiad.olympic_exercises.all())

        context = {
            'olympiad': olympiad,
        }
    except ObjectDoesNotExist:
        context = None

    return render(request, 'olympiad.html', context=context)




def list_exercises(request):
    
    all_exercises = OlympiadExercise.objects.all()

    context = {
        'exercises': all_exercises
    }

    return render(request, 'exercises.html', context=context)




def show_exercise(request, slug):
    
    context = {
        'exercise': OlympiadExercise.objects.get(slug=slug)
        }
    
    return render(request, 'exercise.html', context=context)