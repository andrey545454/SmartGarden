from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def nature_home(request):
    return render(request, 'nature_home.html')


def nature_outside(request):
    return render(request, 'nature_outside.html')


def add_nature(request):
    return render(request, 'add_nature.html')
