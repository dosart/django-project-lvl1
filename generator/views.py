from django.http import request
from django.shortcuts import render

import random


def home(request):
    return render(request, 'generator/home.html', {'password': 'Qwerty1234'})

def password(request):
    password = ''
    length = int(request.GET.get('length'))
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    for _ in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

