from django.contrib import admin

# Register your models here.
from .models import  SupplyChainSelection, User, Organization, ScenarioChanges

admin.site.register(SupplyChainSelection)
admin.site.register(ScenarioChanges)
admin.site.register(User)
admin.site.register(Organization)