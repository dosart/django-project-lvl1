from django.http import request
from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html', {'password': 'Qwerty1234'})

def password(request):
    return render(request, 'generator/password.html', {'password': 'Qwerty1234'})

