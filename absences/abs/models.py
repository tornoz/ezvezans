from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    identifiant = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    class Meta:
        abstract = True

class Etudiant(Utilisateur):
    groupe = models.CharField(max_length=100)
    promotion = models.CharField(max_length=100)

class Enseignant(Utilisateur):
    departement = models.CharField(max_length=200)

class Cours(models.Model):
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    enseignant = models.ForeignKey(Enseignant)
