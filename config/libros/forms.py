from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'fecha_publicacion', 'sinopsis']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'sinopsis': forms.Textarea(attrs={'rows': 4}),
        }