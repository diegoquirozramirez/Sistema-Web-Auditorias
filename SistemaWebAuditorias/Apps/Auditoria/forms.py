from django import forms
from Apps.Auditoria.models import auditoria

class auditoriaForm(forms.ModelForm):
    class Meta:
        model = auditoria

        fields = [
            'codigo' ,
            'nombre',
            'ubic' ,
            'level_risk' ,
            'init_date' ,
            'fini_date' ,
            'inform' ,
        ]

        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control is-valid'}) ,
            'nombre':forms.TextInput(attrs={'class':'form-control is-valid'}) ,
            'ubic' :forms.TextInput(attrs={'class':'form-control is-valid'}),
            'level_risk':forms.TextInput(attrs={'class':'form-control is-valid'}) ,
            'init_date' :forms.TextInput(attrs={'class':'form-control is-valid'}),
            'fini_date' :forms.TextInput(attrs={'class':'form-control is-valid'}),
            #'inform' :forms.TextInput(),
        }