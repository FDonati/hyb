from django.conf import settings
from django.core.management.base import BaseCommand
from labels.models import Region, Product, Indicator, Activity, FinalDemand

import os
import sys


class Command(BaseCommand):
    """
    Populate database with pre developed csv files residing in labels app
    """

    def handle(self, *args, **options):
        try:
            project_root_dir = settings.BASE_DIR
            indicatorData = getfile(os.path.join(
                project_root_dir, 'labels/source/indicators.csv'))
            regionData = getfile(
                os.path.join(project_root_dir, 'labels/source/regions.csv'))
            productData = getfile(
                os.path.join(project_root_dir, 'labels/source/products.csv'))
            finalDemandData = getfile(
                os.path.join(project_root_dir, 'labels/source/final_demand.csv'))
            activityData = getfile(
                os.path.join(project_root_dir, 'labels/source/activities.csv'))


            populate(indicatorData, Indicator, "Indicator")
            populate(regionData, Region, "Region")
            populate(productData, Product, "Product")
            populate(activityData, Activity, "Activity")
            populate(finalDemandData, FinalDemand, "Final demand")
        except Exception as e:
            sys.exit(f"Adding database objects Failed.. {e}")


# function that adds to DB
def addToDB(model, name, code, unit, global_id, parent_id, local_id, level, identifier, leaf_children_global,
               leaf_children_local):
    
    try:
        e, created = model.objects.get_or_create(name=name, code=code, unit=unit, 
                                                global_id=global_id, parent_id=parent_id,
                                                local_id=local_id, level=level, identifier=identifier,
                                                leaf_children_global=leaf_children_global,
                                                leaf_children_local=leaf_children_local)
    except:
        e, created = model.objects.get_or_create(name=name, code=code, unit=unit, 
                                                global_id=global_id, parent_id=parent_id,
                                                local_id=local_id, level=level)

    return e


def populate(data_obj, model, model_type):

    print("Adding values to table: ", model_type)
    counter = 0
    # add children now
    for x in data_obj:
        try:
            name = x[0]
            code = x[1]
            unit = x[2]
            global_id = int(x[3])
            parent_id = int(x[4])
            local_id = int(x[5])
            level = int(x[6])
            identifier = x[7]
            leaf_children_global = x[8]
            leaf_children_local = x[9]
            counter += 1
            
            addToDB(model, name, code, unit, global_id, parent_id, local_id, level, identifier, leaf_children_global,
                        leaf_children_local)
            print("number of records: " + str(counter), end='\r')
        except Exception as e:
            sys.exit(f"Adding database objects Failed.. {e}")
    print("\n")


def getfile(myFile):
    # open the file

    f = open(myFile, 'r')
    # get the content
    F = f.read()
    # split (make an array where each element is determined by an enter)
    U = F.split('\n')
    # Create empty list
    data = []
    # fill the empty list with the data (this time split even further by tabs)
    for line in U:
        data.append(line.split('\t'))
    # remove header and last line -> it is always structured the same
    data.pop(0)
    data.pop(-1)

    return data
