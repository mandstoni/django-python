from django.db import models


class Tipo(models.Model):
    descricao = models.CharField(max_length=100)
    origem = models.CharField(max_length=100)

class Opcao(models.Model):
    descricao = models.CharField(max_length=100)

class Salada(models.Model):
    descricao = models.CharField(max_length=100)
    dcolheita = models.CharField(max_length=100)



class Comida(models.Model):
    tipoComida = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=200)
    quantidade = models.BigIntegerField()
    opcoes = models.ForeignKey(Opcao, on_delete=models.SET_NULL, null=True)
    valorCalorico = models.BigIntegerField()
    salada = models.ForeignKey(Salada, on_delete=models.SET_NULL, null=True)


