import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from core.models import Period, Year
from olympiads.models import Olympiad, OlympiadExercise, Level
from olympiads.forms import ExerciseTypeForm




def define_current_period():
    """
    Defines the current school year.
    """
    current_month = datetime.date.today().month
    current_year = datetime.date.today().year

    if current_month > 8:
        start_year = Year.objects.get(year=current_year)
        end_year = Year.objects.get(year=current_year + 1)
    else:
        start_year = Year.objects.get(year=current_year - 1)
        end_year = Year.objects.get(year=current_year)

    current_period = Period.objects.get(start_year=start_year, end_year=end_year)

    return current_period



def list_olympiads(request):
    '''
    Shows all the olympiads of current period
    '''

    current_period = define_current_period()

    all_olympiads = Olympiad.objects.filter(period=current_period)
    levels = Level.objects.all()

    context = {
        'olympiads': all_olympiads,
        'levels': levels
    }

    return render(request, 'olympiads.html', context=context)



def show_olympiad(request, slug):
    '''
    Shows the olympiad page and exercises related to it
    '''

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
    '''
    Shows all the olympic exercises
    '''
    
    all_exercises = OlympiadExercise.objects.all()

    context = {
        'exercises': all_exercises
    }

    return render(request, 'exercises.html', context=context)



def show_exercise(request, slug):
    '''
    Shows one exercise
    '''
    
    context = {
        'exercise': OlympiadExercise.objects.get(slug=slug)
        }
    
    return render(request, 'exercise.html', context=context)



def create_exercise_type(request):
    '''
    Allows creating exercise types via /create/exercise-type/
    '''

    if request.method == 'POST':

        form =ExerciseTypeForm(request.POST)

        if form.is_valid():

            form.save()

            form = ExerciseTypeForm()

            context = {
                    'form': form
                }

            return render(request, 'create_exercise_type.html', context=context)
        return render(request, 'create_exercise_type.html', context=context)

    else:
        form = ExerciseTypeForm()

        context = {
            'form': form
            }

        return render(request, 'create_exercise_type.html', context=context)