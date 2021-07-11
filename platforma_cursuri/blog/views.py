from django.shortcuts import render
from .models import Articol


def blog(request):
    articole = Articol.objects.order_by('-data_publicare').all()
    return render(request, "blog.html", {"articole":articole})