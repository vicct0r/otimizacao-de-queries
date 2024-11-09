from django.db import models
from django.contrib.auth.models import User


class Academia(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome


class Assinantes(models.Model):
    nome = models.CharField(max_length=60)
    academia = models.ForeignKey(Academia, related_name='assinantes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} assinante da {self.academia.nome}'


