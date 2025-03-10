from django import forms
from django.contrib.auth.models import User
from .models import Matiere

class MatiereAdminForm(forms.ModelForm):
    enseignants = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(profile__role='enseignant'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    etudiants = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(profile__role='etudiant'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Matiere
        fields = '__all__'
