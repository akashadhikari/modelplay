from django.contrib import admin

from .models import Client, ContactPerson, Company


admin.site.register(Client)
admin.site.register(ContactPerson)
admin.site.register(Company)
