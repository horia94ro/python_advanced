from django.shortcuts import render, redirect
from .models import Cheltuiala, Incasare


def homepage(request):
    buget_curent = calculeaza_buget()
    lista_cheltuieli = []
    lista_incasari = []
    cheltuieli = Cheltuiala.objects.all()
    incasari = Incasare.objects.all()
    for cheltuiala in cheltuieli:
        inreg = {"data_inregistrare": cheltuiala.data_inregistrare, "valoare": cheltuiala.valoare}
        lista_cheltuieli.append(inreg)
    for incasare in incasari:
        inreg = {"data_inregistrare": incasare.data_inregistrare, "valoare": incasare.valoare}
        lista_incasari.append(inreg)
    return render(request, "homepage.html", {"cheltuieli": lista_cheltuieli, "incasari": lista_incasari, "buget": buget_curent})


def operatie_noua(request):
    return render(request, "operatie_noua.html")


def inregistreaza_operatie(request):
    data_inregistrare = str(request.GET.get('data_operatie'))
    valoare_inregistrare = int(request.GET.get('valoare'))
    tip_inregistrare = request.GET.get('tip_operatie')
    if tip_inregistrare == "cheltuiala":
        inreg = Cheltuiala(data_inregistrare = data_inregistrare, valoare = valoare_inregistrare)
    else:
        inreg = Incasare(data_inregistrare = data_inregistrare, valoare = valoare_inregistrare)
    inreg.save()
    return redirect("/")


def calculeaza_buget():
    total_incasari = 0
    total_cheltuieli = 0
    cheltuieli = Cheltuiala.objects.all()
    incasari = Incasare.objects.all()
    for cheltuiala in cheltuieli:
        total_cheltuieli += cheltuiala.valoare
    for incasare in incasari:
        total_incasari += incasare.valoare
    buget = total_incasari - total_cheltuieli
    return buget