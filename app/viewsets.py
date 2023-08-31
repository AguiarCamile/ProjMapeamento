from rest_framework import viewsets
from .serializers import CulturasSerializer, ProprietariosSerializer, PropriedadesSerializer
from .models import Culturas, Proprietarios, Propriedades

class CulturasViewSet(viewsets.ModelViewSet):
    model = Culturas
    serializer_class = CulturasSerializer
    queryset = Culturas.objects.all()
    filter_fields = ('TipoCultura')

class ProprietariosViewSet(viewsets.ModelViewSet):
    model = Proprietarios
    serializer_class = ProprietariosSerializer
    queryset = Proprietarios.objects.all()
    filter_fields = ('nomeProprietarios', 'cpf', 'contato')

class PropriedadesViewSet(viewsets.ModelViewSet):
    model = Propriedades
    serializer_class = PropriedadesSerializer
    queryset = Propriedades.objects.all()
    filter_fields = ('Estado', 'Microrregiao', 'Cidade',  'Culturas', 'Proprietarios', 'app', 'rl', 'rl_coordenadas', 'tamanho_area')