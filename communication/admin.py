from django.contrib import admin

from .models import SalesGroup, SubStage, Communication

# Register your models here.

admin.site.register(SalesGroup)
admin.site.register(SubStage)
admin.site.register(Communication)
