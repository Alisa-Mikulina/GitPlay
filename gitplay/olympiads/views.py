from django.shortcuts import render
from core import constants
from olympiads.models import Olympiad


def list_olympiads(request):

    all_olympiads = Olympiad.objects.all()

    context = {
        'olympiads': all_olympiads
    }

    return render(request, 'olympiads.html', context=context)


def show_olympiad(request, id: int):

    if id > len(constants.OLYMPIADS) or id < 1:
        context = {
            'id': id,
            'olympiads': constants.OLYMPIADS
        }
    else:

        olympiad = Olympiad.objects.filter(id=id)
        olympiad_vals = olympiad.values_list()

        context = {
            'id': id,
            'name': olympiad_vals[0][1],
            'lvl': olympiad_vals[0][2],
            'olympiads': Olympiad.objects.all()
        }

    return render(request, 'olympiad.html', context=context)

