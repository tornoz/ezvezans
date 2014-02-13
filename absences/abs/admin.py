from django.contrib import admin
from abs.models import Absence
from abs.models import Etudiant
from abs.models import Enseignant
from abs.models import Cours
from abs.models import Justificatif
from abs.models import Secretaire


class UtilisateurAdmin(admin.ModelAdmin):
    # ...
    list_display = ('identifiant', 'user')
    

admin.site.register(Absence)
admin.site.register(Etudiant, UtilisateurAdmin)
admin.site.register(Enseignant, UtilisateurAdmin)
admin.site.register(Cours)
admin.site.register(Justificatif)
admin.site.register(Secretaire, UtilisateurAdmin)
