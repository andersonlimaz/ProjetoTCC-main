
from django.db import models

class ONG(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    nome_comercial = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)  # Defina unique=True para evitar duplicatas
    celular = models.CharField(max_length=14)  # Assuming you want to store the phone number as a string
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Defina unique=True para evitar duplicatas
    senha = models.CharField(max_length=255)
    senha2 = models.CharField(max_length=255)
   
   

    
    # Outros campos do seu modelo aqui

    def __str__(self):
        return self.nome_fantasia  # Isso define como o objeto ONG será representado quando convertido em string


class Pagamento(models.Model):
    forma_pagamento = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    ong_parceiras = models.CharField(max_length=255)
    data_pagamento = models.DateField()