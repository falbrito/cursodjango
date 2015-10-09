# -*- coding: utf-8 -*-
from django.contrib import admin
from aula8.models import Contact

class ContactAdmin(admin.ModelAdmin):
	date_hierarchy = 'birthday' # Vai ordernar por data de nascimento

	# Controla visualização de campos
	# fields = ('name', 'birthday')
	# ou
	# exclude = ('info',)

	list_filter = ('active',) # para gerar um filtro ao lado

	list_display = ('name','birthday','active')

# registro o model
admin.site.register(Contact, ContactAdmin)
