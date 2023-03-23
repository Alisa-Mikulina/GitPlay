from django.shortcuts import render
from olympiads.models import Olympiad
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

        context = {
            'olympiad': olympiad
        }
    except ObjectDoesNotExist:
        context = None

    return render(request, 'olympiad.html', context=context)

