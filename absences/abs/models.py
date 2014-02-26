from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm



# Create your models here.
class Utilisateur(models.Model):
    identifiant = models.CharField(max_length=200)
    user = models.ForeignKey(User);
    class Meta:
        abstract = True
    def __str__(instance):
        return instance.identifiant
    def get_fullname(instance):
        name = instance.user.first_name + ' ' + instance.user.last_name
        if name == ' ':
            name = instance.user.__str__
        return name
	
class Groupe(models.Model):
    departement = models.CharField(max_length = 100)
    specialite = models.CharField(max_length = 100)
    annee = models.IntegerField()
    groupe = models.IntegerField()
    def __str__(instance):
        return instance.departement + instance.annee.__str__() + ' ' + instance.specialite + instance.groupe.__str__()

class Etudiant(Utilisateur):
    groupe = models.ForeignKey(Groupe)
    @staticmethod
    def get_from_user(django_user):
        try:
            return Etudiant.objects.get(user=django_user)
        except Etudiant.DoesNotExist:
            return -1
    

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
    @staticmethod
    def get_from_user(django_user):
        try:
            return Secretaire.objects.get(user=django_user)
        except Secretaire.DoesNotExist:
            return -1

class Cours(models.Model):
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    enseignant = models.ForeignKey(Enseignant)
    groupe = models.ManyToManyField(Groupe)
    matiere = models.CharField(max_length = 100)
    def __str__(instance):
        return instance.dateDebut.__str__() + '->' + instance.dateFin.__str__() + ' : ' + instance.matiere + '(' + instance.enseignant.__str__() + ')'
    
class Absence(models.Model):
    cours = models.ForeignKey(Cours)
    etudiant = models.ForeignKey(Etudiant)
    def __str__(instance):
        return instance.cours.matiere.__str__() + '(' + instance.etudiant.__str__() +')'
    def est_justifiee(instance):
        query = Justificatif.objects.filter(etudiant=instance.etudiant)
        query = query.filter(valide = True)
        query = query.filter(dateDebut__lt = instance.cours.dateDebut)
        query = query.filter(dateFin__gt = instance.cours.dateFin)
        if(query.count() > 0):
            return True
        else:
            return False

class Justificatif(models.Model):
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    etudiant = models.ForeignKey(Etudiant)
    valide = models.BooleanField(default=False)
    fichier=models.FileField(upload_to="justificatifs", null=True)
