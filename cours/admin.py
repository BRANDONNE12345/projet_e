from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Matiere, Chapitre, Contenu, Quiz, Question, Note, Profile

# Enregistre les modèles classiques
admin.site.register(Matiere)
admin.site.register(Chapitre)
admin.site.register(Contenu)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Note)

# Profile admin classique
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

# On désenregistre et réenregistre le modèle User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
