from django.contrib import admin

from .models import \
    Client, \
    SalesGroup, \
    SubStage, \
    Communication, \
    Lead, \
    LeadStage, \
    LeadPost


admin.site.register(Client)
admin.site.register(SalesGroup)
admin.site.register(SubStage)
admin.site.register(Communication)
admin.site.register(Lead)
admin.site.register(LeadStage)
admin.site.register(LeadPost)



