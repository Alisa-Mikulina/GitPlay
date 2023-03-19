from django.shortcuts import render
from core import constants


def main(request):
    return render(request, 'main.html')