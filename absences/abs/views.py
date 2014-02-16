from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.contrib.auth.models import User, Group
from abs.models import Etudiant, Enseignant, Secretaire, Cours, Justificatif, Absence
from django.forms.models import modelformset_factory

@login_required
def index(request):
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
