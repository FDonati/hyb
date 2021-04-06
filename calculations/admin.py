from django.contrib import admin
from .models import Job #, Country, Product, Indicator, ModellingProduct
import pandas as pd

# Register your models here.
admin.site.register(Job)
# admin.site.register(Country)
# admin.site.register(Product)
# admin.site.register(Indicator)
# admin.site.register(ModellingProduct)

stock = pd.read_csv("data/MR_HIOT_2011_v3_3_18_11_stock_to_waste.csv")
