from django.shortcuts import render
from core import constants


def main(request):
    return render(request, 'main.html')


def list_olympiads(request):

    context = {
        'olympiads': constants.OLYMPIADS
    }

    return render(request, 'olympiads.html', context=context)


def list_team(request):

    context = {
        'team': constants.TEAM
    }

    return render(request, 'team.html', context=context)