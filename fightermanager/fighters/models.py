from django.db import models

# Create your models here.
class Fighter(models.Model):
    name = models.Charfield(max_length=100)
    nickname = models.Charfield(max_length=100)