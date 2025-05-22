from django import forms
from .models import Atividade, Relatorio

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['titulo', 'tipo', 'data_inicio']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }

class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['atividade', 'arquivo']
        widgets = {
            'atividade': forms.Select(attrs={'class': 'form-control'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
