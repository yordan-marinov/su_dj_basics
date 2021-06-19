from django.urls import path

from crm.views import crm_lead_list


urlpatterns = [
    path('', crm_lead_list, name='crm_lead_list')
]
