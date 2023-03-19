from django.shortcuts import render
from core import constants


def list_olympiads(request):

    context = {
        'olympiads': constants.OLYMPIADS
    }

    return render(request, 'olympiads.html', context=context)