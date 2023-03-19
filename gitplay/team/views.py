from django.shortcuts import render
from core import constants



def list_team(request):

    context = {
        'team': constants.TEAM
    }

    return render(request, 'team.html', context=context)