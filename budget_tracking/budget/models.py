from django.db import models


class Cheltuiala(models.Model):
    data_inregistrare = models.DateField()
    valoare = models.FloatField()


class Incasare(models.Model):
    data_inregistrare = models.DateField()
    valoare = models.FloatField()
