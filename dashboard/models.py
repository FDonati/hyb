from django.db import models

# Create your models here.
class SupplyChain(models.Model):
    source1 = models.TextField()
    source2 = models.TextField()
    target1 = models.TextField()
    value   = models.DecimalField(decimal_places=2, max_digits=5)
    target2 = models.TextField()
    unit    = models.TextField(default="what up!")