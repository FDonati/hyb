from django.contrib import admin

# Register your models here.
from .models import  Region, ModellingProduct, Product, Indicator

admin.site.register(Region)
admin.site.register(ModellingProduct)
admin.site.register(Product)
admin.site.register(Indicator)