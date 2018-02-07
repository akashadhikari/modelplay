from django.contrib import admin

from .models import SalesGroup, SubStage, Communication, ContactPerson

# Register your models here.

admin.site.register(SalesGroup)
admin.site.register(SubStage)
admin.site.register(Communication)
admin.site.register(ContactPerson)
