
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from paginas.apps import PaginasConfig
from .models import ONG
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from .models import ONG, Pagamento
from django.http import HttpResponse

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "index.html"

class Doe(TemplateView):
    template_name ="about-us.html"

class Servicos(TemplateView):
    template_name = "services.html"

class Blog(TemplateView):
    template_name = "blog.html"

class Contato(TemplateView):
    template_name = "contact-us.html"
    
class Formulario(TemplateView):
    template_name = "formulario.html"    







def cadastro_ong(request):
    if request.method == 'POST':
        # Obtain the form data
        nome_fantasia = request.POST.get('firstname')
        nome_comercial = request.POST.get('lastname')
        cnpj = request.POST.get('cnpj')
        celular = request.POST.get('number')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')

        # Create an instance of the ONG model and save it to the database
        ong = ONG(
            nome_fantasia=nome_fantasia,
            nome_comercial=nome_comercial,
            cnpj=cnpj,
            celular=celular,
            endereco=endereco,
            cidade=cidade,
            email=email,
            senha=senha,
            senha2=senha2,
            
        )
        ong.save()

        # Set a success message in the session variable
        request.session['mensagem_sucesso'] = 'Cadastro realizado com sucesso.'
        
        # Redirect to a success page (replace 'servicos' with the URL of your success page)
        return redirect('servicos')
    else:
        request.session['mensagem_sucesso'] = 'Cadastro não realizado.'

        return render(request, 'formulario.html')  # Make sure the template name is correct
    
def pagamento_ong(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        forma_pagamento = request.POST.get('forma_pagamento')
        valor = request.POST.get('valor')
        ong_parceiras = request.POST.get('subject')

        if forma_pagamento == 'pix':
            forma_pagamento='pix'
        elif forma_pagamento =='boleto':
            forma_pagamento = 'boleto'

        if ong_parceiras == 'Empresa 1':
           ong_parceiras = 'Empresa 1'
        elif ong_parceiras == 'Empresa 2':
            ong_parceiras = 'Empresa 2'
        elif ong_parceiras == 'Empresa 3':
            ong_parceiras = 'Empresa 3'

       

        # Create an instance of the ONG model and save it to the database
        pagamento = Pagamento(
            nome=nome,
            email=email,
            forma_pagamento=forma_pagamento,
            valor=valor,
            ong_parceiras=ong_parceiras,
        )
        pagamento.save()

        # Set a success message in the session variable
        request.session['mensagem_sucesso'] = 'Pagamento realizado com sucesso.'
        
        # Redirect to a success page (replace 'servicos' with the URL of your success page)
        return redirect('servicos')
    else:
        request.session['mensagem_sucesso'] = 'Pagamento não realizado.'

        return render(request, 'formulario.html')  # Make sure the template name is correct 



