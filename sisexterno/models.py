# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cpf = models.CharField(unique=True, max_length=11)
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=60)
    nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    nacionalidade = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    numero_cartao = models.CharField(max_length=16)
    titular_cartao = models.CharField(max_length=60)
    validade_cartao = models.DateField()
    codigo_seguranca = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'cliente'
