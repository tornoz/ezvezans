from django.db import models
from abs.models import Justificatif
from django.forms import ModelForm
from django import forms

class JustificatifForm(ModelForm):
    class Meta:
        model = Justificatif
        #file  = forms.FileField()
       # fields = ['etudiant', 'dateDebut', 'dateFin', 'valide', 'file']
        
