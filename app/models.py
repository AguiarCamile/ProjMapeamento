from django.db import models

# Create your models here.
class Culturas(models.Model):
    TipoCultura = models.CharField(max_length=40)
    def __str__(self):
        return self.TipoCultura

class Proprietarios(models.Model):
    nomeProprietarios = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    contato = models.CharField(max_length=13)

    def __str__(self):
        return self.nomeProprietarios

class Propriedades(models.Model):
    Estado = models.CharField(max_length=40)
    Microrregiao = models.CharField(max_length=40)
    Cidade = models.CharField(max_length=40)
    Culturas = models.ForeignKey(Culturas, on_delete=models.CASCADE)
    Proprietarios = models.ForeignKey(Proprietarios, on_delete=models.CASCADE)
    app = models.CharField(max_length=20)
    rl = models.CharField(max_length=50)
    rl_coordenadas = models.CharField(max_length=13)
    tamanho_area = models.CharField(max_length=11)

    def __str__(self):
        return "Propriedade {}".format(self.id)