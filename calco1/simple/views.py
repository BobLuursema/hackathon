from django.shortcuts import render
from django.http import JsonResponse
from . import models as m
import operator

# Create your views here.
def regelingen(request):
    data = m.RegelingOpties.objects.values()
    return JsonResponse(dict(regelingopties=list(data)))

def suggesties(request, id):
    p = m.Persoon.objects.get(pk=id)
    reg = {k: {'aanvraag': 15, 'wijzigen': 0, 'informatie': 0} for k in list(m.Regelingen.objects.values_list('naam', flat=True))}
    for r in p.regelingen.all():
        reg[r.naam]['aanvraag'] -= 500
        reg[r.naam]['wijzigen'] += 100
    if p.ontslagaanvraag:
        reg['WW']['aanvraag'] += 10
        reg['WW']['informatie'] += 20
    if p.leeftijd > 40:
        reg['Ziekte']['aanvraag'] += 10
        reg['Ziekte']['informatie'] += 20
        reg['Zwanger']['aanvraag'] -= 15
        reg['Zwanger']['informatie'] -= 15
    if p.geslacht == 'V':
        reg['Zwanger']['aanvraag'] += 10
        reg['Zwanger']['informatie'] += 20
    semi_results = {}
    for r in reg:
        for f in reg[r]:
            semi_results["{} {}".format(r,f)] = reg[r][f]
    results = {'data':[]}
    for k, v in sorted(semi_results.items(), key=operator.itemgetter(1)):
        if k[k.index(' ')+1:] == 'aanvraag':
            url = m.Regelingen.objects.get(naam=k[:k.index(' ')]).insert_url
        elif k[k.index(' ')+1:] == 'informatie':
            url = m.Regelingen.objects.get(naam=k[:k.index(' ')]).info_url
        elif k[k.index(' ')+1:] == 'wijzigen':
            url = m.Regelingen.objects.get(naam=k[:k.index(' ')]).update_url
        results['data'].append({k: url})
    results['data'].reverse()
    return JsonResponse(results)