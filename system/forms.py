from django import forms
from . import models


class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = ('__all__')
        exclude = ('location',)

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Name of the Medicine'}),
            'generic_name':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Generic name of the Medicine'}),
            'mg_dose':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'500 MG'}),
            'stock':forms.NumberInput(attrs={'class':'form-control mt-2', 'placeholder':'100'}),
            'exipiry_date':forms.TextInput(attrs={'type':'date','class':'form-control mt-2', 'placeholder':'Name of the Medicine'}),
            'manufacture_date':forms.TextInput(attrs={'type':'date','class':'form-control mt-2', 'placeholder':'Name of the Medicine'}),
        }

