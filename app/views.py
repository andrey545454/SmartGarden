from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def nature(request):
    return render(request, 'nature.html')
