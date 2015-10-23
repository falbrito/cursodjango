# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse # para chamar ao inves da URL chamar o nome da URL

class TestIndexView(TestCase):
	# TestIndexView é uma nomenclatura utilizada pelo Alisson

	def setUp(self):
		self.url = reverse('aula9_index') # utiliza o alias de aula9 definido em urls.py

    # A função setUp serve para definir variáveis. 
    # Pois numa execução podem existir diversos testes de URL.

	def test_render(self):
		response = self.client.get(self.url)
		print response
		self.assertEquals(response.status_code, 200)
		self.assertEquals(response.content, u'Aula9') # que é a informaçao vinda de aula9/views.py
		# diz que o teste tem que retornar 200
