from django.shortcuts import render
from django.views.generic import ListView
from main.models import *

def hoomepage(request):
    return render(request, './base_generic.html')

class SladoledList(ListView):
    model = Sladoled


class NapitakList(ListView):
    model = Napitak

def filerSladoledi(request):
    data  = Sladoled.objects.filter(naziv__startswith='M')

    context = {'sladoledi' : data}
    return render(request, 'filterS.html', context = context)

def filerNapitci(request):
    data  = Napitak.objects.filter(naziv__startswith='M')

    context = {'napitci' : data}
    return render(request, 'filterN.html', context = context)