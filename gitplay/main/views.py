from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def list_olympiads(request):

    OLYMPIADS = [
        'Всероссийская олимпиада школьников ',
        'Ломоносов',
        'Покори Воробьевы горы!',
        'Высшая проба',
        'СПбГУ',
        'РАНХиГС',
        'Евразийская',
        'Учитель школы будущего',
        'РГГУ',
        'Герценовская',
        'Ведомственная',
        'Челябинская',
        'Плехановская',
        'Миссия выполнима'
    ]

    context = {
        'olympiads': OLYMPIADS
    }

    return render(request, 'olympiads.html', context=context)


def list_team(request):
    
    TEAM = [
        'Яковлева Екатерина',
        'Микулина Алиса',
        'Рехкайнен Александра',
        'Титова Вероника',
        'Шубкина Анна',
        'Молчанов Василий',
        'Бикмаметова Карина',
        'Снименко Юлия'
    ]

    context = {
        'team': TEAM
    }

    return render(request, 'team.html', context=context)