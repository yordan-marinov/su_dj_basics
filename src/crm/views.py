from typing import ContextManager
from django.shortcuts import redirect, render

from crm.forms import LeadForm

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


def create_lead(request):
    form = LeadForm(request.POST or None)
    if form.is_valid():
        agent = Agent.objects.first()
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        age = form.cleaned_data['age']
        lead = Lead(
            first_name=first_name,
            last_name=last_name,
            age=age,
            agent=agent, 
        )
        lead.save()
        return redirect('crm_lead_list')
    
    context = {
        'form': form,
    }
    return render(request, 'crm/crm_create_lead.html', context)