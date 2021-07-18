from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'first_app/homepage.html')

def nume_animale(request):
    valori = {
        "pisica_bland_female" : ["Leia", "Sheba", "Terra", "Luna", "Mi", "Izzy"],
        "pisica_bland_male" : ["Oreo", "Ash", "Coco", "Oscar", "Ziggy", "Milo"],
        "pisica_fioros_female" : ["Xena", "Yara", "Nessie", "Crystal", "Lucy"],
        "pisica_fioros_male" : ["Ghost", "Fangs", "Loki", "Shadow", "Styx"],
        "catel_bland_female" : ["Ava", "Bella", "Cleo", "Cora", "Kira"],
        "catel_bland_male" :  ["Bolt", "Aslan", "Clifford", "Marty", "Piper"],
        "catel_fioros_female" :  ["Buffy", "Amber", "Arya", "Storm", "Onyx"],
        "catel_fioros_male" : ["Spike", "Blitz", "Wolf", "Brutus", "Beast"]
    }

    tip_animal = request.GET.get('tip_animal')
    fioros = request.GET.get('fioros')
    fioros = "fioros" if fioros else "bland" #Această logică suplimentară este necesară deoarece valoarea lui fioros va fi None în cazul în care checkbox-ul din formular nu este bifat.
    male_female = request.GET.get('mascul_femela')
    cheie = tip_animal + "_" + fioros + "_" + male_female
    nume_final = random.choice(valori[cheie])
    return render(request, 'first_app/nume_animale.html',
                  {'nume_final' : nume_final})