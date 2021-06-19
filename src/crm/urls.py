from django.urls import path

from crm.views import create_lead, crm_lead_list, delete_lead, details_agent, details_lead


urlpatterns = [
    path('', crm_lead_list, name='crm_lead_list'),
    path('<int:pk>', details_lead, name='crm_lead_details'),
    path('agent/<int:pk>', details_agent, name='crm_agent_details'),
    path('create/', create_lead, name='crm_lead_create'),
    path('delete/<int:pk>', delete_lead, name='crm_lead_delete'),
]
