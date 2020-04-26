from .models import Review
from django import forms
from django.forms import widgets

class Multistep(forms.ModelForm):
    class Meta:
        model=Review
        fields=['BasicCheckup','ElectricalCheckup','MechanicalCheckup','InstallationCheckup','ChilledwaterCheckup','Name']
        widgets = { 'BasicCheckup': forms.TextInput(attrs={'size': 200}),'ElectricalCheckup':forms.TextInput(attrs={'size': 200}),

'MechanicalCheckup': forms.TextInput(attrs={'size': 200}),'InstallationCheckup': forms.TextInput(attrs={'size': 200}),'ChilledwaterCheckup': forms.TextInput(attrs={'size': 200}),'Name': forms.TextInput(attrs={'size': 200})
        }
           