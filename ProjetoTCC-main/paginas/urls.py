
from django.urls import path 
from .views import PaginaInicial, Doe, Servicos, Blog, Contato, Formulario, cadastro_ong
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

   
    path('cadastro_ong/', views.cadastro_ong, name='cadastro_ong'),
]

    



    
