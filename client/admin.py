from django.contrib import admin

from .models import Client, SalesGroup, SalesStage, Communication

# Register your models here.

admin.site.register(Client)
admin.site.register(SalesGroup)
admin.site.register(SalesStage)
admin.site.register(Communication)