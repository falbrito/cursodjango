# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required

# importa o forms aula7.forms
from aula7.forms import LoginForm


def index(request):
	next = request.REQUEST.get('next', '/aula7/')
	# primeiro procura no request.GET e depois procura no request.POST

	# se existir o valor para o parametro next ele pega
	# caso contrario passa o valor '/aula7/'
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			# Se o usuário é válido eu logo esse usuário
			user = form.save() # retorna as informações de usuario e senha
			login(request, user)
			# return HttpResponseRedirect(reverse('aula7_index'))
			# Usando o redirecionamento para 'next'
			return HttpResponseRedirect(next)

	else:
		form = LoginForm()
	return render(request, 'aula7/index.html',
		{
			'form' : form,
			'next' : next,
		}
	)

def sair(request):
	logout(request)
	return HttpResponseRedirect(reverse('aula7_index'))

@login_required
def view_protegida(request):
	return HttpResponse('View protegida!')

@permission_required('aula5.add_categoria')
def view_protegida2(request):
	return HttpResponse('View protegida2!')


