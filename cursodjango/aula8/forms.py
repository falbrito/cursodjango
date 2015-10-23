# -*- coding: utf-8 -*-
from django import forms

from aula8.models import Contact

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact

	def clean_name(self): 
	    #iremos criar uma validação para o nome. Iremos proibir o nome "luke"
		name = self.cleaned_data.get('name')
		if name == 'luke':
			raise forms.ValidationError(u'Esse nome é proibido')
		return name