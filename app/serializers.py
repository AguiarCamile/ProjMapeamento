from .models import Culturas, Proprietarios, Propriedades
from rest_framework import serializers

class CulturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culturas
        fields = ["TipoCultura"]


class ProprietariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietarios
        fields = ['nomeProprietarios', 'cpf', 'contato']


class PropriedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedades
        fields = ['Estado', 'Microrregiao', 'Cidade',  'Culturas', 'Proprietarios', 'app', 'rl', 'rl_coordenadas', 'tamanho_area']
