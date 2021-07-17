from django.shortcuts import render, redirect
from .models import Cheltuiala, Incasare
from datetime import date

def homepage(request):
    cheltuieli = Cheltuiala.objects.all().order_by('-data_inregistrare')
    incasari = Incasare.objects.all().order_by('-data_inregistrare')
    buget_curent = calculeaza_buget(cheltuieli, incasari)
    return render(request, "homepage.html",
                  {"cheltuieli": cheltuieli, "incasari": incasari, "buget": buget_curent})


def operatie_noua(request):
    data_curenta = str(date.today())
    return render(request, "operatie_noua.html", {"data_curenta": data_curenta})


def inregistreaza_operatie(request):
    data_inregistrare = str(request.GET.get('data_operatie'))
    valoare_inregistrare = float(request.GET.get('valoare'))
    tip_inregistrare = request.GET.get('tip_operatie')
    if tip_inregistrare == "cheltuiala":
        inreg = Cheltuiala(data_inregistrare=data_inregistrare, valoare=valoare_inregistrare)
    else:
        inreg = Incasare(data_inregistrare=data_inregistrare, valoare=valoare_inregistrare)
    inreg.save()
    return redirect("/")


def calculeaza_buget(cheltuieli, incasari):
    total_incasari = 0
    total_cheltuieli = 0
    for cheltuiala in cheltuieli:
        total_cheltuieli += cheltuiala.valoare
    for incasare in incasari:
        total_incasari += incasare.valoare
    buget = total_incasari - total_cheltuieli
    return buget
