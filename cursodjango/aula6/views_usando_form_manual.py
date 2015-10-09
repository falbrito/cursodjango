# -*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from aula6.models import Contact
from aula6.forms import ContactForm

def index(request):
    contatos = Contact.objects.all()

    if request.method == 'POST':
    	form = ContactForm(request.POST)
    	if form.is_valid():
    		# processa o formulario

    		# Agora está usando o método save criado em forms.py
    		novo_contato = form.save()

    		return HttpResponseRedirect(reverse('aula6_index'))
    else:
    	form = ContactForm()

    return render(request, 'aula6/index.html',
        {
            'contatos': contatos,
            'form': form
        }

    )

def detail(request, id):
    contato = get_object_or_404(Contact, id=id)
    initial = {
    	'first_name': contato.first_name,
    	'last_name': contato.last_name,
    	'email': contato.email,
    	'twitter': contato.twitter
    }
    if request.method == 'POST':
    	form = ContactForm(request.POST)
    	if form.is_valid():
    		novo_contato = form.save(contato=contato)
    		return HttpResponseRedirect(reverse('aula6_index'))
    else:
    	form = ContactForm(initial=initial)

    return render(request, 'aula6/detail.html',
        {
            'contato': contato,
            'form': form,
        }

    )
