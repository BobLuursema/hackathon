from django.shortcuts import render
from django.http import JsonResponse
from . import models as m

# Create your views here.
def regelingen(request):
    data = m.Regeling.objects.values()
    return JsonResponse(dict(regelingen=list(data)))

def suggesties(request, naam=None):
    p = m.Persoon.objects.get(naam=naam)
    data = []
    return JsonResponse({"hoi": naam})