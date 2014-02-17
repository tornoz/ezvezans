from django.contrib import admin
from abs.models import Absence
from abs.models import Etudiant
from abs.models import Enseignant
from abs.models import Cours
from abs.models import Justificatif
from abs.models import Secretaire
from abs.models import Groupe

class UtilisateurAdmin(admin.ModelAdmin):
    # ...
    list_display = ('identifiant', 'user')
    
    
class GroupeAdmin(admin.ModelAdmin):
    # ...
    list_display = ('__str__','departement', 'specialite', 'annee', 'groupe')
    
   

admin.site.register(Absence)
admin.site.register(Etudiant, UtilisateurAdmin)
admin.site.register(Enseignant, UtilisateurAdmin)
admin.site.register(Cours)
admin.site.register(Justificatif)
admin.site.register(Secretaire, UtilisateurAdmin)
admin.site.register(Groupe, GroupeAdmin)
