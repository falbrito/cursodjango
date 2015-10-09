# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):

	name = models.CharField(
		u'Nome',
		max_length=100,
	)

	birthday = models.DateField(
		u'Aniversário',
		null=False, # não pode ser nulo
		blank=False, # não pode ser vazio
	)

	info = models.TextField(
		u'Informações do contato'
	)

	active = models.BooleanField(
		u'Contanto ativo',
		default=True,
		help_text=u'Marque para definir o contato como ativo.'
	)

	def __unicode__(self): # informação que retornará 
		return self.name

	class Meta: # Troca o que for "Contact" por "Contato" ou "Contatos"
		verbose_name = u'Contato'
		verbose_name_plural = u'Contatos'
		ordering = ['name']



