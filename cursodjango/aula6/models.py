# -*- coding: utf-8 -*-
from django.db import models

class Contact(models.Model):

	first_name = models.CharField(
		u'Nome',
		max_length=30
	)
	last_name = models.CharField(
		u'Sobrenome',
		max_length=30
	)
	email = models.EmailField(
		u'E-mail',
		max_length=75
	)
	twitter = models.URLField(
		u'Twitter',
		max_length=200
	)

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

