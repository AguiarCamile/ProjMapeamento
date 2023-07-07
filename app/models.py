from django.db import models

# Create your models here.
class Culturas(models.Model):
    Cultura = models.CharField(max_length=45)

class Proprietarios(models.Model):
    nomeProprietarios = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    contato = models.CharField(max_length=13)

class Propriedades(models.Model):
    Culturas_id = models.ForeignKey(Culturas, to_field='id', on_delete=models.CASCADE)
    Proprietarios_id = models.ForeignKey(Proprietarios, to_field='id', on_delete=models.CASCADE)
    app = models.CharField(max_length=10)
    rl = models.CharField(max_length=10)
    rl_coord = models.CharField(max_length=13)
    tamanho_area = models.CharField(max_length=11)