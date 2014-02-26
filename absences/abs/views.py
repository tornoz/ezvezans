from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.contrib.auth.models import User, Group
from abs.models import Etudiant, Enseignant, Secretaire, Cours, Justificatif, Absence
from django.forms.models import modelformset_factory
from abs.forms import JustificatifForm
from django.forms.widgets import HiddenInput
from datetime import datetime, timedelta

@login_required
def index(request):
    if request.user.__str__() == "admin":
        return redirect('/admin')
    
    groups = request.user.groups.values_list('name',flat=True)
    
    template = loader.get_template('dashboard/report/' + groups[0] + '.html')
    name = request.user.first_name + ' ' + request.user.last_name
    if name == ' ':
        name = request.user
    var = {
        'user_name': name,
        'title':'Accueil',
        'groupname':groups[0],
    }
    
    if groups[0] == "enseignant":
        var['enseignant'] = Enseignant.get_from_user(request.user) 
        var['cours'] = Cours.objects.filter(enseignant = var['enseignant'])
        var['absences'] = Absence.objects.filter(cours__in=var['cours'])
        Formset = modelformset_factory(Absence)
        var['formset'] = Formset(queryset=Absence.objects.none())
        #Limite les cours à ceux de l'enseignant
        var['formset'].forms[0].fields['cours'].queryset = Cours.objects.filter(enseignant = var['enseignant'])
        total_absences =  var['absences'].count()
        total_cours =  var['cours'].count()
        if total_cours != 0:
            var['absences_moyennes'] = total_absences/total_cours
        else:
            var['absences_moyennes'] = "Pas de cours"
        cours = Cours.objects.filter(enseignant = var['enseignant']).filter(dateDebut__gt = datetime.today()-timedelta(days=15))
        var['absents_derniers_jours'] = Absence.objects.filter(cours__in = cours).count()
    elif groups[0] == "etudiant":
        var['etudiant'] = Etudiant.get_from_user(request.user)
        var['absences'] = Absence.objects.filter(etudiant = var['etudiant'])
        var['justif_attente'] = Justificatif.objects.filter(etudiant = var['etudiant'])
        JustificatifFormset = modelformset_factory(Justificatif,widgets={'etudiant':HiddenInput, 'valide':HiddenInput})
        #TODO make a more secure way to add justificatif, cause here a simple modification and the student can send a validated justficatif for another student... 
        var['justificatif_formset'] = JustificatifFormset(queryset=Justificatif.objects.none(), initial=[{'valide': False, 'etudiant':var['etudiant']}])
        var['stat_absences_total'] = var['absences'].count()
        justi = 0
        non_justi = 0
        for a in var['absences'].all():
            if a.est_justifiee():
                justi = justi +1
            else:
                non_justi = non_justi +1
        var['stat_absences_justifiees'] = justi
        var['stat_absences_non_justifiees'] = non_justi
    else :
        var['secretaire'] = Secretaire.get_from_user(request.user)
        var['justi_attente'] = Justificatif.objects.filter(valide=False)
        var['justi_derniers'] = Justificatif.objects.filter(valide=True)
        JustificatifFormset = modelformset_factory(Justificatif)
        var['justificatif_formset'] = JustificatifFormset(queryset=Justificatif.objects.none(), prefix="justificatif")
        CoursFormset = modelformset_factory(Cours)
        var['cours_formset'] = CoursFormset(queryset=Cours.objects.none(),  prefix="cours")
        
    context = RequestContext(request, var)
          
    
    return HttpResponse(template.render(context))
    


def add(request, entity):
    entity_array = {'enseignant':Enseignant, 'etudiant':Etudiant,'secretaire':Secretaire, 'cours':Cours, 'justificatif':Justificatif, 'absence':Absence}
    Formset = modelformset_factory(entity_array[entity])
    
    if request.method == "POST":
        if 'prefix' in request.POST:
            prefix = request.POST['prefix']
        else:
            prefix = ""
        formset = Formset(request.POST, request.FILES, prefix = prefix)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return redirect('/abs')
        else:
            return redirect('/abs')
    else:
        template = loader.get_template('dashboard/form.html')
        name = request.user.first_name + ' ' + request.user.last_name
        context = RequestContext(request, {
            'user_name': name,
            'title':'Formulaire',
            'formset':Formset(entity_array[entity].objects.none()),
            'entity_name':entity
        })
        return HttpResponse(template.render(context))

def ajax_absent(request, coursid):
    if request.is_ajax():
        cours = Cours.objects.get(id=coursid)
        groupes = cours.groupe.all()
        etudiants = Etudiant.objects.filter(groupe__in=groupes)
        #On récupere les etudiants déjà absents à ce cours
        absences = Absence.objects.filter(cours=cours)
        absents = []
        for a in absences:
            absents.append(a.etudiant)
        print(absents)
        string = ""
        for e in etudiants:
            if e not in absents:
                fullname = e.user.first_name + ' ' + e.user.last_name;
                if fullname == ' ':
                    fullname = e.user.__str__()
                string += (fullname + "," + e.user.__str__() + ";")
        return HttpResponse(string)
    return redirect('/abs')


def ajax_insert_absent(request, coursid, etudiantid):
    if True:#request.is_ajax():
        cours = Cours.objects.get(id=coursid)
        user = User.objects.get(username=etudiantid)
        etudiant = Etudiant.objects.get(user=user)
        absence = Absence(cours = cours, etudiant = etudiant)
        absence.save()
        latest = Absence.objects.latest('id');
        reponse = ""
        if absence.est_justifiee():
            reponse = "t"
        else:
            reponse = "f"
        reponse += latest.id.__str__()
        return HttpResponse(reponse)
    return redirect('/abs')
    
def ajax_delete(request,table, id):
    entity_array = {'enseignant':Enseignant, 'etudiant':Etudiant,'secretaire':Secretaire, 'cours':Cours, 'justificatif':Justificatif, 'absence':Absence}
    if request.is_ajax():
        e = entity_array[table](id=id)
        e.delete()
        return HttpResponse("ok")
    return redirect('/abs')
    
def validate_justificatif(request, justid):
    justificatif = Justificatif.objects.get(id=justid)
    justificatif.valide = True
    justificatif.save()
    return redirect('/abs')
