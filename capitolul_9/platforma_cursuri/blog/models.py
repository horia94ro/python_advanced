from django.db import models

class Articol(models.Model):
    titlu = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    continut = models.TextField()
    data_publicare = models.DateField()
