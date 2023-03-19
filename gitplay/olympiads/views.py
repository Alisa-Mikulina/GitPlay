from django.shortcuts import render
from core import constants


def list_olympiads(request):

    context = {
        'olympiads': constants.OLYMPIADS
    }

    return render(request, 'olympiads.html', context=context)


def show_olympiad(request, id: int):

    if id > len(constants.OLYMPIADS) or id < 1:
        context = {
            'id': id,
            'olympiads': constants.OLYMPIADS
        }
    else:
        context = {
            'id': id,
            'olympiad': constants.OLYMPIADS[id - 1],
            'olympiads': constants.OLYMPIADS
        }

    return render(request, 'olympiad.html', context=context)

