from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About',
        'content': 'О нас',
        'text': 'Магазин мебели HOME создан в 2023 году'
    }
    return render(request, 'main/about.html', context)


