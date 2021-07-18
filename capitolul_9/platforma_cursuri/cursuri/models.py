from django.db import models

class Curs(models.Model):
    nume = models.CharField(max_length = 50) #50 reprezintă lungimea maximă suportată de acest atribut
    descriere = models.TextField()
    imagine = models.ImageField(upload_to = 'cursuri/imagini/')
    url = models.URLField(blank = True)