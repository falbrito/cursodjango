# -*- coding: utf-8 -*-
from django.contrib import admin

from aula8.models import Contact, Phone
from aula8.forms import ContactForm # Importado formulario personalisado

# defino antes de ContactAdmin
# usando TabularInline
class PhoneInline(admin.TabularInline):
	model = Phone

# usando StackedInline
# class PhoneInline(admin.StackedInline):
#	model = Phone

class ContactAdmin(admin.ModelAdmin):
	date_hierarchy = 'birthday' # Vai ordernar por data de nascimento

	# Controla visualização de campos
	# fields = ('name', 'birthday')
	# ou
	# exclude = ('info',)

	list_filter = ('active',) # para gerar um filtro ao lado

	list_display = ('name','birthday','active')

	form = ContactForm

	# incluir campo para pesquisa
	# no exemplo vamos pesquisa no campo nome
	search_fields = ['name']

	inlines = [
		PhoneInline,
	]

# registro o model
admin.site.register(Contact, ContactAdmin)
