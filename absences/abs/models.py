from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Utilisateur(models.Model):
    identifiant = models.CharField(max_length=200)
    user = models.ForeignKey(User);
    class Meta:
        abstract = True

class Etudiant(Utilisateur):
    groupe = models.CharField(max_length=100)
    promotion = models.CharField(max_length=100)

class Enseignant(Utilisateur):
    departement = models.CharField(max_length=200)
    
class Secretaire(Utilisateur):
	departement = models.CharField(max_length=200)

class Cours(models.Model):
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    enseignant = models.ForeignKey(Enseignant)
    
class Absence(models.Model):
    cours = models.ForeignKey(Cours)
    etudiant = models.ForeignKey(Etudiant)

class Justificatif(models.Model):
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    etudiant = models.ForeignKey(Etudiant)
   

