# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Exemplo passando parametro pela URL - por POST
#----------------------------------------------------------
@csrf_exempt # necessario para chamar a biblioteca, e é com @ mesmo!
def index(request):
    if request.method == 'POST':
    	nome = request.POST.get('name', u'não tem nome') # Nunca voltará 'não tem nome'
    	return HttpResponse(u'O nome é %s' % nome)
    else:
        formulario = '''
        <form action="." method="post">
            <input type="text" name="name" maxlength="100" />
            <button type="submit">Enviar</button>
        </form>
        '''
        return HttpResponse(formulario)

# Quando passamos um id pela URL
# Ex.: http://127.0.0.1:8000/aula3/231/
def detail_id(request, id):
	return HttpResponse(u'O id é: %s' % id)

# Quando passamos um id pela URL
# Ex.: http://127.0.0.1:8000/aula3/231/
def detail_username(request, username):
	return HttpResponse(u'O username é: %s' % username)


# Exemplo passando parametro pela URL - por GET
#----------------------------------------------------------
# Ex. 127.0.0.1:8000/aula3/?nome=fabio&idade=42
# def index(request):
#     nome = request.GET.get('nome', u'Não tem nome')
#     idade = request.GET.get('idade', u'Não tem idade')
#     return HttpResponse(u'O nome é %s, a idade é %s'  % (nome, idade))



# Exemplo passando parametro pela URL
#----------------------------------------------------------
# Ex. 127.0.0.1:8000/aula3/?nome=fabio
# def index(request):
#     nome = request.GET.get('nome', u'Não tem nome')
#     return HttpResponse(u'O nome é %s' % nome)

# Exemplo pegar tudo que foi passado por GET na url
#----------------------------------------------------------
# def index(request):
#     lista = request.GET.items()
#     return HttpResponse(lista)

# http://127.0.0.1:8000/aula3/?nome=fabio
# retornara (u'nome', u'fabio')




# Exemplo Olá Mundo
#----------------------------------------------------------
# forma didática
# def index(request):
#    response = HttpResponse()
#    response.write(u'Olá Mundo!')
#    return response

# ou da seguinte forma mais resumida
# def index(request):
#     return HttpResponse(u'Olá Mundo!')

#----------------------------------------------------------