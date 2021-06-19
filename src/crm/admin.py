from django.contrib import admin

from .models import Agent, Lead


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "agent")
