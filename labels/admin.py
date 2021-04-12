from django.contrib import admin

# Register your models here.
from .models import  Country, ModellingProduct, Product, Indicator

admin.site.register(Country)
admin.site.register(ModellingProduct)
admin.site.register(Product)
admin.site.register(Indicator)