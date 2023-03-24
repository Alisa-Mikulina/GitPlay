from django.shortcuts import render
from olympiads.models import Olympiad, OlympiadExercise
from django.core.exceptions import ObjectDoesNotExist

def list_olympiads(request):

    all_olympiads = Olympiad.objects.all()

    context = {
        'olympiads': all_olympiads
    }

    return render(request, 'olympiads.html', context=context)


def show_olympiad(request, slug):

    try:
        olympiad = Olympiad.objects.get(slug=slug)
        print(olympiad.olympic_exercises.all())

        context = {
            'olympiad': olympiad,
            'exercises': olympiad.olympic_exercises.all()
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