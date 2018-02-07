from django.contrib import admin

from .models import Lead, LeadPost, LeadStage

# Register your models here.

admin.site.register(Lead)
admin.site.register(LeadStage)
admin.site.register(LeadPost)