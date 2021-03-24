from django.db import models

# Create your models here.
class SupplyChainSelection(models.Model):
    supply_chain = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    primary = models.BooleanField(default=False)

class ScenarioChanges(models.Model):
    source1 = models.CharField(max_length=50)
    source2 = models.CharField(max_length=50)
    target1 = models.CharField(max_length=50)
    value   = models.DecimalField(decimal_places=2, max_digits=5)
    target2 = models.CharField(max_length=50)
    unit    = models.CharField(max_length=50, default="what up!")


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)


class Organization(models.Model):
    organization_name = models.CharField(max_length=50)
    admin_first_name = models.CharField(max_length=50)
    admin_last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
