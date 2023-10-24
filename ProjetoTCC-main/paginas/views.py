
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from paginas.apps import PaginasConfig
from .models import ONG
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from .models import ONG, Pagamento
from django.http import HttpResponse
from decimal import Decimal, InvalidOperation
from django.contrib import messages
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

class pix(TemplateView):
    template_name = "pix.html"

class boleto(TemplateView):
    template_name = "boleto.html"

class login(TemplateView):
    template_name = "login.html"
    


from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import ONG
from django.views.generic import TemplateView

# Resto do seu código...

class Formulario(TemplateView):
    template_name = "formulario.html"




def cadastro_ong(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome_fantasia = request.POST.get('firstname')
        nome_comercial = request.POST.get('lastname')
        cnpj = request.POST.get('cnpj')
        celular = request.POST.get('number')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')

        # Verifique se o e-mail já existe no banco de dados
        if ONG.objects.filter(email=email).exists():
            # E-mail duplicado, exibir uma mensagem de erro
            return render(request, 'formulario.html', {'error_message': 'Este e-mail já está em uso.'})

        if ONG.objects.filter(cnpj=cnpj).exists():
            # CNPJ duplicado, exibir uma mensagem de erro
            return render(request, 'formulario.html', {'error_message2': 'Este CPNJ já está cadastrado.'})

        # Caso contrário, crie uma instância do modelo ONG e salve-a no banco de dados
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

        # Defina uma mensagem de sucesso na variável de sessão
        request.session['mensagem_sucesso'] = 'Cadastro realizado com sucesso.'

        # Redirecione para uma página de sucesso (substitua 'servicos' pela URL de sua página de sucesso)
        return redirect('servicos')
    else:
        request.session['mensagem_sucesso'] = 'Cadastro não realizado.'

    return render(request, 'formulario.html')  # Certifique-se de que o nome do modelo esteja correto



def pagamento_ong(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        forma_Pagamento = request.POST.get('forma_Pagamento')
        valor = request.POST.get('valor')
        valor = valor.replace(',', '$').replace('.', '$').replace('$', '.')
        try:
            valor_decimal = Decimal(valor)  # Converta para Decimal
        except InvalidOperation:
            valor_decimal = None
        ong_parceiras = request.POST.get('subject')

        if forma_Pagamento == 'pix':
            forma_Pagamento='pix'
        elif forma_Pagamento =='boleto':
            forma_Pagamento = 'boleto'

        if ong_parceiras == 'Empresa 1':
           ong_parceiras = 'Empresa 1'
           
        elif ong_parceiras == 'Empresa 2':
            ong_parceiras = 'Empresa 2'
        elif ong_parceiras == 'Empresa 3':
            ong_parceiras = 'Empresa 3'

        Cadastro_Pagamento = Pagamento.objects.create(            
            nome=nome,
            email=email,
            forma_Pagamento=forma_Pagamento,
            valor=valor,
            ong_parceiras=ong_parceiras) 
        Cadastro_Pagamento.save()
        messages.success(request, 'Pagamento realizado com sucesso!')
        
        if forma_Pagamento == 'pix':
            forma_Pagamento='pix'
            return redirect('pix/')  # Redireciona para a página do Pix
        elif forma_Pagamento == 'boleto':
            forma_Pagamento = 'boleto'
            return redirect('inicio') 



from django.shortcuts import render
from .models import Pagamento

def tabela_view(request):
    dados = Pagamento.objects.all()
    return render(request, 'exibir_pagamentos.html', {'dados': dados})




from django.shortcuts import render
from .models import Pagamento

def tabela_view(request):
    dados = Pagamento.objects.all()
    return render(request, 'exibir_pagamentos.html', {'dados': dados})
