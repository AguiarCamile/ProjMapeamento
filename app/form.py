from django.forms import ModelForm
from django import forms
from app.models import Culturas, Proprietarios, Propriedades

# Create the form class.
class CulturasForm(ModelForm):
    class Meta:
        model = Culturas
        fields = ["TipoCultura"]


class ProprietariosForm(ModelForm):
    class Meta:
        model = Proprietarios
        fields = ['nomeProprietarios', 'cpf', 'contato']


class PropriedadesForm(ModelForm):
    Culturas = forms.ModelChoiceField(queryset=Culturas.objects.all())
    Proprietarios = forms.ModelChoiceField(queryset=Proprietarios.objects.all())

    class Meta:
        model = Propriedades
        fields = ['Estado', 'Microrregiao', 'Cidade',  'Culturas', 'Proprietarios', 'app', 'rl', 'rl_coordenadas', 'tamanho_area', 'satelite']
