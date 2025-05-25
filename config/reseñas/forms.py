from django import forms
from .models import Reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['calificacion', 'comentario']
        widgets = {
            'calificacion': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }
