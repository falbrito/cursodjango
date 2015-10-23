# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from aula7.forms import LoginForm

def index(request):
	# return HttpResponse(u'Aula9')
	return render(request, 'aula9/index.html')
