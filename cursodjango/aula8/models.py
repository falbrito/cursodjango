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
		u'Contato ativo',
		default=True,
		help_text=u'Marque para definir o contato como ativo.'
	)

	def __unicode__(self): # informação que retornará 
		return self.name

	class Meta: # Troca o que for "Contact" por "Contato" ou "Contatos"
		verbose_name = u'Contato'
		verbose_name_plural = u'Contatos'
		ordering = ['name']
		# ordering = ['-name'] Z para A


class Phone(models.Model):

	contact = models.ForeignKey(
		Contact,
		verbose_name=u'Contato',
	)

	description = models.CharField(
		u'Descrição',
		max_length=100,
	)

	phone = models.CharField(
		u'Telefone',
		max_length=20,
	)

	def __unicode__(self): # retornaremos nome e telefone
		return '%s %s' % (self.contact.name, self.phone)

	class Meta:
		verbose_name = u'Telefone'
		verbose_name_plural = u'Telefones'
		

