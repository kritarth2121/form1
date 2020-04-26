from django.db import models
from django.forms import ModelForm
from django import forms

class Review(models.Model):

    BasicCheckup=models.CharField(max_length=100)
    ElectricalCheckup= models.CharField(max_length=100)
    MechanicalCheckup=models.CharField(max_length=100)
    InstallationCheckup=models.CharField(max_length=100)

    ChilledwaterCheckup=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)