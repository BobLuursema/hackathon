from django.shortcuts import render
from django.http import JsonResponse
from . import models as m
import operator

# Create your views here.
def regelingen(request):
    data = m.Regelingen.objects.values_list('naam', flat=True)
    return JsonResponse(dict(regelingen=list(data)))

def persoon(request, id):
    p_naam = m.Persoon.objects.get(pk=id).naam
    p_regelingen = m.Persoon.objects.get(pk=id).regelingen.values_list('naam', flat=True)
    return JsonResponse(dict(naam=p_naam, regelingen=list(p_regelingen)))

def suggesties(request, id):
    p = m.Persoon.objects.get(pk=id)
    reg = {k: 0 for k in list(m.Regelingen.objects.values_list('naam', flat=True))}
    for r in p.regelingen.all():
        reg[r.naam] -= 500
    if p.ontslagaanvraag:
        reg['WW'] += 20
    if p.leeftijd > 40:
        reg['Ziekte'] += 20
        reg['Zwanger'] -= 15
    if p.geslacht == 'V':
        reg['Zwanger'] += 20
    results = {'data':[]}
    for k, v in sorted(reg.items(), key=operator.itemgetter(1)):
        url = m.Regelingen.objects.get(naam=k).info_url
        results['data'].append({k: url})
    results['data'].reverse()
    results['data'] = results['data'][:2]
    return JsonResponse(results)