from typing import ContextManager
from django.shortcuts import get_object_or_404, redirect, render

from crm.forms import LeadForm, LeadModelForm

from .models import Agent, Lead


def crm_lead_list(request):
    qs = Lead.objects.all()
    context = {"leads": qs, "page_name": "leads"}
    return render(request, "crm/crm_lead_list.html", context)


def details_lead(request, pk):
    obj = Lead.objects.get(pk=pk)
    context = {"lead": obj, "page_name": "leads"}
    return render(request, "crm/crm_lead_details.html", context)


def details_agent(request, pk):
    obj = Agent.objects.get(pk=pk)
    print(obj)
    context = {"agent": obj}
    return render(request, "crm/crm_agent_details.html", context)


def create_lead_form(request):
    form = LeadForm(request.POST or None)
    if form.is_valid():
        agent = Agent.objects.first()
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        age = form.cleaned_data["age"]
        lead = Lead(
            first_name=first_name,
            last_name=last_name,
            age=age,
            agent=agent,
        )
        lead.save()
        return redirect("crm_lead_list")

    context = {
        "form": form,
    }
    return render(request, "crm/crm_create_lead.html", context)


def create_lead(request):
    form = LeadModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("crm_lead_list")

    context = {
        "form": form,
        "page_name": "Create Page",
    }
    return render(request, "crm/crm_create_lead.html", context)


def delete_lead(request, pk):
    
    obj = get_object_or_404(Lead, pk=pk)
    form = LeadForm(initial=obj.__dict__)
    # form = LeadModelForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("crm_lead_list")

    context = {'lead': obj, 'form': form}
    return render(request, "crm/crm_lead_delete.htm", context)


def edit_lead(request, pk):
    obj = Lead.objects.get(pk=pk)
    form = LeadModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("crm_lead_list")

    context = {
        "form": form,
        'lead': obj,
        "page_name": "Edit Lead",
    }
    return render(request, "crm/crm_lead_edit.html", context)
