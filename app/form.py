from django.forms import ModelForm
from django import forms
from app.models import Culturas, Proprietarios, Propriedades

# Create the form class.
class CulturasForm(ModelForm):
    class Meta:
        model = Culturas
        fields = ["Cultura"]


class ProprietariosForm(ModelForm):
    class Meta:
        model = Proprietarios
        fields = ['nomeProprietarios', 'cpf', 'contato']

class PropriedadesForm(ModelForm):
    Culturas_id = forms.ModelChoiceField(queryset=Culturas.objects.all())
    Proprietarios_id = forms.ModelChoiceField(queryset=Proprietarios.objects.all())
    class Meta:
        model = Propriedades
        fields = ['Culturas_id', 'Proprietarios_id','app', 'rl', 'rl_coord', 'tamanho_area']