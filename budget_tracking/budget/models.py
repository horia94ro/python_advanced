from django.db import models

class Cheltuiala(models.Model):
    data_inregistrare = models.CharField(max_length=100)
    valoare = models.IntegerField()

class Incasare(models.Model):
    data_inregistrare = models.CharField(max_length=100)
    valoare = models.IntegerField()
