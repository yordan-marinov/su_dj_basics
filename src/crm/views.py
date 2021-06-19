from django.shortcuts import render

from .models import Lead


def crm_lead_list(request):
    qs = Lead.objects.all()
    context = {
        'leads': qs, 
        'page_name': 'leads'
        }
    return render(request, "crm/crm_lead_list.html", context)


def details_lead(request, pk):
    pass
    