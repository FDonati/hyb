from django.core.management.base import BaseCommand
from labels.models import Region, Product, Indicator, Activity, FinalDemand


class Command(BaseCommand):
    """
    Clear database command
    """

    def handle(self, *args, **options):
        print("***removing hierarchies out of DB***")
        Region.objects.all().delete()
        Product.objects.all().delete()
        Indicator.objects.all().delete()
        Activity.objects.all().delete()
        FinalDemand.objects.all().delete()