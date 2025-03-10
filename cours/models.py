from django.db import models
from django.contrib.auth.models import User

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    enseignants = models.ManyToManyField(User, related_name='matieres_enseignees')
    etudiants = models.ManyToManyField(User, related_name='matieres_suivies')

    def __str__(self):
        return self.nom

class Chapitre(models.Model):
    titre = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Contenu(models.Model):
    type_contenu = models.CharField(max_length=50)
    data = models.TextField()
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)

    def __str__(self):
        # Affiche le type de contenu et un extrait des 50 premiers caractères de data
        return f"{self.type_contenu}: {self.data[:50]}..."  # Limite l'affichage à 50 caractères


class Quiz(models.Model):
    titre = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    nombreTentatives = models.IntegerField(default=1)
    correctionAutomatique = models.BooleanField(default=False)

    def __str__(self):
        # Affiche le titre du quiz et la matière associée
        return f"{self.titre} - Matière: {self.matiere.nom}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    contenu = models.TextField()

    def __str__(self):
        # Affiche le titre du quiz et un extrait du contenu de la question
        return f"Quiz: {self.quiz.titre} - Question: {self.contenu[:50]}..."  # Limite l'affichage à 50 caractères


class Note(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()

class Profile(models.Model):
    USER_ROLES = [
        ('etudiant', 'Étudiant'),
        ('enseignant', 'Enseignant'),
        ('admin', 'Administrateur'),
        ('compta', 'Comptabilité'),
        ('scolarite', 'Responsable Scolarité'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
