from django import forms
from django.core.exceptions import ValidationError

from .models import Lead

def positive_digit(value):
    if value < 1:
        raise ValidationError('The age must be a positive number')


class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    age = forms.IntegerField(validators=[positive_digit,])
    
     
