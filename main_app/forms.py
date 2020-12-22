from django.forms import ModelForm
from .models import Wearing

class WearingForm(ModelForm):
    class Meta:
        model = Wearing
        fields = ['date', 'mood']