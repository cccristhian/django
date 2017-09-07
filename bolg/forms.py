from django import forms

from .models import Publicar

class postearForm(forms.ModelForm):

        class Meta:
            model = Publicar
            fields = ('titulo', 'texto',)
#/de querer todos los campos s
#olo debe de dejar en blanco los parentesis
