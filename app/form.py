from django.forms import ModelForm
from app.models import Estados

# Create the form class.
class EstadosForm(ModelForm):
     class Meta:
        model = Estados
        fields = ["Estado"]
