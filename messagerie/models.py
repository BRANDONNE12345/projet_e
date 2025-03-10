from django.db import models
from django.contrib.auth.models import User
from cours.models import Matiere

class Chat(models.Model):
    participants = models.ManyToManyField(User)
    matiere = models.ForeignKey(Matiere, on_delete=models.SET_NULL, null=True, blank=True)

class Forum(models.Model):
    titre = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

class Message(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, blank=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True, blank=True)
