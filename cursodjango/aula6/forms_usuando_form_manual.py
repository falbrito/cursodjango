# -*- coding: utf8 -*-
from django import forms

from aula6.models import Contact

class ContactForm(forms.Form):
	first_name = forms.CharField(label='Nome', max_length=30)
	last_name = forms.CharField(label='Sobrenome', max_length=30)
	email = forms.EmailField(label='E-mail', max_length=75)
	twitter = forms.URLField(label='Twitter', max_length=200)

	# definindo metodo save
	def save(self, contato=None):
   		nome = self.cleaned_data.get('first_name')
   		sobrenome = self.cleaned_data.get('last_name')
   		email = self.cleaned_data.get('email')
   		twitter = self.cleaned_data.get('twitter')
   		# Se contato existe carrega os campos
   		if contato:
   			contato.first_name = nome
   			contato.last_name = sobrenome
   			contato.email = email
   			contato.twitter = twitter
   			contato.save()
   			return contato
   		# Se contato não existe então cria novo
   		else:
   			novo_contato = Contact(
	   			first_name=nome,
   				last_name=sobrenome,
   				email=email,
   				twitter=twitter
			)
   			novo_contato.save()
   			return novo_contato

   	# metódo para validar e-mail já cadastrado
   	def clean_email(self):
   		email = self.cleaned_data.get('email')
   		# Pesquisa na planilha do banco de dados se já existe o e-mail
   		if Contact.objects.filter(email=email):
   			raise forms.ValidationError(u'Email já cadastrado.')
   		return email

   	# metódo para validar twitter já cadastrado
   	def clean_twitter(self):
   		twitter = self.cleaned_data.get('twitter')
   		# Pesquisa na planilha do banco de dados se já existe o twitter
   		if Contact.objects.filter(twitter=twitter):
   			raise forms.ValidationError(u'Twitter já cadastrado.')
   		return twitter