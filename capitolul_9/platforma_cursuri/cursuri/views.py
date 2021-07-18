from django.shortcuts import render
from .models import Curs

def homepage(request):
    cursuri = Curs.objects.all() #Aici realizăm operația de extragere a tuturor înregistrărilor din baza de date
    return render(request, "homepage.html", {"cursuri":cursuri})

