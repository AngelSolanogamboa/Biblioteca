# forms.py
from django import forms
from .models import Prestamo
from datetime import date, timedelta

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'fecha_vencimiento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_vencimiento'].initial = date.today() + timedelta(days=7)
