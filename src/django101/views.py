# Model View Template (MVP)
from django.shortcuts import render

from .form import ContactForm


def home_page(request):
    context = {"title": "Hello there...", "page_name": "home"}

    return render(request, "home_page.html", context)


def about_page(request):
    context = {"title": "About us", "page_name": "about"}

    return render(request, "about_page.html", context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    
    context = {
        "title": "Contact us", 
        "page_name": "contacts",
        'form': form,
        }

    return render(request, "form.html", context)
