from django import forms
from django.contrib.auth.models import User
from .models import Mensaje


class FormularioMensaje(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Para',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'cuerpo']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }