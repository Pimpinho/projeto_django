from django.db import models

class Ufs(models.Model):
    id_uf = models.AutoField(primary_key=True)
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)

class Cidades(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome_cidade = 
    if_uf

class Enderecos(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    id_cidade = 
    logradouro
    numero
    cep
    bairro
    complemento
    observacoes

class Contas(models.Model):
    id_conta = models.AutoField(primary_key=True)
    tp_conta
    id_banco
    banco
    conta
    agencia
    operacao

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username
    first_name
    last_name
    
class Pessoas(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    vinculo
    id_user
    cpf
    nome 
    telefone
    e-mail
    id_endereco
    id_conta

class Ocorrencias(models.Model):
    id_ocorrencia = models.AutoField(primary_key=True)
    data
    realizada
    ocorrencia
    id_pessoa
