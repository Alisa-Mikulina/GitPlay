from django.shortcuts import render
from core import constants



def list_team(request):

    context = {
        'team': constants.TEAM
    }

    return render(request, 'team.html', context=context)


def team_member(request, name:str):

    context = {
        'name': name
    }

    return render(request, 'team_member.html', context=context)