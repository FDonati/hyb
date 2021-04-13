from django.contrib import admin

# Register your models here.
from .models import  Region, FinalDemand, Product, Indicator, Activity

admin.site.register(Region)
admin.site.register(FinalDemand)
admin.site.register(Product)
admin.site.register(Indicator)
admin.site.register(Activity)