from django.contrib import admin

from .models import Lead, LeadPost, LeadStage, SalesLead


admin.site.register(Lead)
admin.site.register(LeadStage)
admin.site.register(LeadPost)
admin.site.register(SalesLead)