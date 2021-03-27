from django.contrib import admin

# Register your models here.
from .models import  SupplyChainSelection, User, Organization, ScenarioChange

admin.site.register(SupplyChainSelection)
admin.site.register(ScenarioChange)
admin.site.register(User)
admin.site.register(Organization)