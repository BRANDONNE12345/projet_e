from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Matiere, Chapitre, Contenu, Quiz, Question, Note, Profile
from .forms import MatiereAdminForm  # Ton formulaire personnalisé

# Personnalisation Matiere
class MatiereAdmin(admin.ModelAdmin):
    form = MatiereAdminForm

admin.site.register(Matiere, MatiereAdmin) # Enregistre directement sans unregister

# Autres modèles (inchangés)
admin.site.register(Chapitre)
admin.site.register(Contenu)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Note)
admin.site.register(Profile)

# Personnalisation avancée de l'affichage User/Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role')

    def get_role(self, instance):
        return instance.profile.get_role_display()
    get_role.short_description = 'Rôle'

# Réenregistrement du modèle User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
