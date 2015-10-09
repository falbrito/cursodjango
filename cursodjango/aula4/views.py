# -*- coding: utf-8 -*-
from django.shortcuts import render # Funcao para renderizar templates

def index(request):
    lista = [
        u'Alisson',
        u'Fábio',
        u'João'
    ]
    
    # 1 - request
    # 2 - template
    # 3 - variaveis
    return render(request, 'aula4/index.html', {'lista': lista})