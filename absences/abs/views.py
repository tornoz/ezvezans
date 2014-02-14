from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.contrib.auth.models import User, Group

@login_required
def index(request):
    groups = request.user.groups.values_list('name',flat=True)
    print(groups)
    template = loader.get_template('report/' + 'enseignant' + '.html')
    name = request.user.first_name + ' ' + request.user.last_name
    if name == ' ':
        name = request.user
    context = RequestContext(request, {
        'user_name': name
    })
    return HttpResponse(template.render(context))
