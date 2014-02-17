from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.contrib.auth.models import User, Group
from abs.models import Etudiant, Enseignant, Secretaire, Cours, Justificatif, Absence
from django.forms.models import modelformset_factory
from abs.forms import JustificatifForm

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
        print(var['absences'])
    elif groups[0] == "etudiant":
        var['etudiant'] = Etudiant.get_from_user(request.user)
        var['absences'] = Absence.objects.filter(etudiant = var['etudiant'])
    else :
        var['secretaire'] = Secretaire.get_from_user(request.user)
        var['justificatifs'] = Justificatif.objects.filter(valide=False)
    context = RequestContext(request, var)
          
    
    return HttpResponse(template.render(context))
    


def add(request, entity):
    entity_array = {'enseignant':Enseignant, 'etudiant':Etudiant,'secretaire':Secretaire, 'cours':Cours, 'justificatif':Justificatif, 'absence':Absence}
    formset = modelformset_factory(entity_array[entity])
    template = loader.get_template('dashboard/form.html')
    name = request.user.first_name + ' ' + request.user.last_name
    context = RequestContext(request, {
        'user_name': name,
        'title':'Formulaire',
        'formset':formset,
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
    if request.is_ajax():
        cours = Cours.objects.get(id=coursid)
        user = User.objects.get(username=etudiantid)
        etudiant = Etudiant.objects.get(user=user)
        absence = Absence(cours = cours, etudiant = etudiant)
        absence.save()
        return HttpResponse("ok")
    return redirect('/abs')
    
def ajax_delete_absent(request, id):
    if request.is_ajax():
        absence = Absence(id=id)
        absence.delete()
        return HttpResponse("ok")
    return redirect('/abs')
    
def add_justificatif(request):
    formset = modelformset_factory(Justificatif, form=JustificatifForm)
    template = loader.get_template('dashboard/form.html')
    name = request.user.first_name + ' ' + request.user.last_name
    context = RequestContext(request, {
        'user_name': name,
        'title':'Formulaire',
        'formset':formset,
        'entity_name':'justificatif'
    })
    return HttpResponse(template.render(context))
