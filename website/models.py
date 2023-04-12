from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    word = models.CharField(max_length=50)

    def __str__(self):
        return f"\"{self.word}\" belonging to {self.user.username}"

class Definition(models.Model):
    definition = models.TextField()
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=True)


class Example(models.Model):
    text = models.TextField()
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)
