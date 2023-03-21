from django.shortcuts import render
from olympiads.models import Olympiad


def list_olympiads(request):

    all_olympiads = Olympiad.objects.all()

    context = {
        'olympiads': all_olympiads
    }

    return render(request, 'olympiads.html', context=context)


def show_olympiad(request, id: int):

    all_olympiads = Olympiad.objects.all()

    if id > len(all_olympiads) or id < 1:
        
        return render(request, 'olympiad.html')

    else:

        olympiad = Olympiad.objects.filter(id=id)
        olympiad_vals = olympiad.values_list()

        context = {
            'id': id,
            'name': olympiad_vals[0][1],
            'lvl': olympiad_vals[0][2],
        }

    return render(request, 'olympiad.html', context=context)

