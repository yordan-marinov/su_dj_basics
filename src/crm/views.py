from typing import ContextManager
from django.shortcuts import render

from .models import Agent, Lead


def crm_lead_list(request):
    qs = Lead.objects.all()
    context = {
        'leads': qs, 
        'page_name': 'leads'
        }
    return render(request, "crm/crm_lead_list.html", context)


def details_lead(request, pk):
    obj = Lead.objects.get(pk=pk)
    context = {'lead': obj, 'page_name': 'leads'}
    return render(request, 'crm/crm_lead_details.html', context)
    

def details_agent(request, pk):
    obj = Agent.objects.get(pk=pk)
    print(obj)
    context = {'agent': obj}
    return render(request, 'crm/crm_agent_details.html', context)