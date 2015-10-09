# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):

	username = forms.CharField(
		label='Nome de Usuário',
		max_length=30
	)

	password = forms.CharField(
		label='Senha',
		max_length=30,
		widget=forms.PasswordInput # Utilizado para não deixar aparecer o que é digitado
	)

	# Validando o usuário
	def clean_username(self):
		username = self.cleaned_data.get('username')

		# Verifica se usuário existe
		# quando utiliza "User.objects.filter" não é preciso usar try - except
		# se eu usar "User.objects.get" então será necessário usar try - except
		if not User.objects.filter(username=username):
			raise forms.ValidationError(u'Esse nome de usuário não existe.')
		return username

	# Validando a senha
	def clean_password(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if not authenticate(username=username, password=password):
			raise forms.ValidationError(u'Senha incorreta.')
		return password

	def save(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		return authenticate(username=username, password=password)