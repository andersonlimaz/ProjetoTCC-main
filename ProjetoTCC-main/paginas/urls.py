
from django.urls import path 
from .views import PaginaInicial, Doe, Servicos, Blog, Contato, Formulario, cadastro_ong, pagamento_ong, pix, boleto, Login, Usuario, fazerLogin
from django.urls import path
from . import views

urlpatterns = [ 
    # Sempre que for criar path caminho 
    #path('endereço', MinhaView.as_view(), name='Nome-da-url'),
    path('', PaginaInicial.as_view(), name='inicio'),
    path('doe/', Doe.as_view(), name='doe'),
    path('servicos/', Servicos.as_view(), name='servicos'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contato/', Contato.as_view(), name='contato'),
    path('formulario/', Formulario.as_view(), name='formulario'),
    path('login/', Login.as_view(), name='login'),
    path('usuario/', Usuario.as_view(), name='usuario'),


    path('pix/', pix.as_view(), name='pix/'),
    path('boleto/', boleto.as_view(), name='boleto'),

    path('fazerLogin', views.fazerLogin, name='fazerLogin'),
    path('cadastro_ong/', views.cadastro_ong, name='cadastro_ong'),
    # ROTA CADASTRO PAGAMENTO. 
    path('pagamento_ong/', views.pagamento_ong, name='pagamento_ong'),

]

    


    
