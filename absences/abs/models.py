from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Utilisateur(models.Model):
    identifiant = models.CharField(max_length=200)
    user = models.ForeignKey(User);
    class Meta:
        abstract = True


class Promotion(models.Model):
    department = models.CharField(max_length = 100)
    specialite = models.CharField(max_length = 100)
    annee = models.IntegerField()

class Etudiant(Utilisateur):
    groupe = models.CharField(max_length=100)
    promotion = models.ForeignKey(Promotion)

class Enseignant(Utilisateur):
    departement = models.CharField(max_length=200)
    
    @staticmethod
    def get_from_user(django_user):
        try:
            return Enseignant.objects.get(user=django_user)
        except Enseignant.DoesNotExist:
            return -1
            
class Secretaire(Utilisateur):
	departement = models.CharField(max_length=200)

class Cours(models.Model):
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    enseignant = models.ForeignKey(Enseignant)
    promotion = models.ManyToManyField(Promotion)
    matiere = models.CharField(max_length = 100)
    
class Absence(models.Model):
    cours = models.ForeignKey(Cours)
    etudiant = models.ForeignKey(Etudiant)

class Justificatif(models.Model):
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    etudiant = models.ForeignKey(Etudiant)
    valide = models.BooleanField()
