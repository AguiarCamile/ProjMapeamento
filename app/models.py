from django.db import models

# Create your models here.
class Culturas(models.Model):
    Cultura = models.CharField(max_length=45)

class Proprietarios(models.Model):
    nomeProprietarios = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    contato = models.CharField(max_length=13)
