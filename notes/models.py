from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_users = models.ManyToManyField(User, related_name='shared_notes', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class NoteChange(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
