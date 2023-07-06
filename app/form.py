from django.forms import ModelForm
from app.models import Culturas, Proprietarios

# Create the form class.
class CulturasForm(ModelForm):
    class Meta:
        model = Culturas
        fields = ["Cultura"]


class ProprietariosForm(ModelForm):
    class Meta:
        model = Proprietarios
        fields = ['nomeProprietarios', 'cpf', 'contato']
