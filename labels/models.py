from django.db import models

# Create your models here.



class Region(models.Model):
    """
    Region model to store identifiers for the countries and aggregations
    """

    # The name of the country
    name = models.CharField(max_length=200)
    
    # The country code
    code = models.CharField(max_length=20)
    
    # The unit used for the indicator
    unit = models.CharField(max_length=20, null=True)

    # The global id representing the application coordinates as primary id
    global_id = models.IntegerField()
    
    # The id representing what parent this country belongs to (by parent global_id)
    parent_id = models.IntegerField()
    
    # The local id, only used if the hierarchy level is the lowest
    local_id = models.IntegerField()
    
    #The level of hierarchy this country is in
    level = models.IntegerField()
    
    # an identifier determining if it is a leaf node or aggregate
    identifier = models.CharField(max_length=20)
    
    # the global id's of the leafs for this continent (if available)
    leaf_children_global = models.CharField(max_length=2000)
    
    # the local id's of the leafs of this country (if available)
    leaf_children_local = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model to store identifiers for the products and aggregations
    """

    # The name of the product category
    name = models.CharField(max_length=200)

    # The product category code
    code = models.CharField(max_length=20)

    # The global id representing the application coordinates as primary id
    global_id = models.IntegerField()

    # The unit used for the indicator
    unit = models.CharField(max_length=20, null=True)

    # The id representing what parent this product belongs to (by parent global_id)
    parent_id = models.IntegerField()
    
    # The local id, only used if the hierarchy level is the lowest
    local_id = models.IntegerField()
    
    # The level of hierarchy this product is in
    level = models.IntegerField()
    
    # an identifier determining if it is a leaf node or aggregate
    identifier = models.CharField(max_length=20)

    # the global id's of the leafs for this product group (if available)
    leaf_children_global = models.CharField(max_length=2000)

    # the local id's of the leafs of this product group (if available)
    leaf_children_local = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Activity(models.Model):
    """
    Product model to store identifiers for the products and aggregations
    """

    # The name of the activity
    name = models.CharField(max_length=200)
    
    # The product category code
    code = models.CharField(max_length=20)
    
    # The unit used for the activity
    unit = models.CharField(max_length=20, null=True)
    
    # The global id representing the application coordinates as primary id
    global_id = models.IntegerField()

    # The id representing what parent this product belongs to (by parent global_id)
    parent_id = models.IntegerField()
    
    # The local id, only used if the hierarchy level is the lowest
    local_id = models.IntegerField()
    
    # The level of hierarchy this product is in
    level = models.IntegerField()
    
    # an identifier determining if it is a leaf node or aggregate
    identifier = models.CharField(max_length=20)
     
    # the global id's of the leafs for this product group (if available)
    leaf_children_global = models.CharField(max_length=2000)
    
    # the local id's of the leafs of this product group (if available)
    leaf_children_local = models.CharField(max_length=2000)
    

    def __str__(self):
        return self.name


class FinalDemand(models.Model):
    """
    Modelling data-model to store identifiers for the products and aggregations (slight modified version of Product)
    """

    # The name of the product category
    name = models.CharField(max_length=200)
    
    # The product category code
    code = models.CharField(max_length=20)
    
    # The unit used for the activity
    unit = models.CharField(max_length=20, null=True)
    
    # The global id representing the application coordinates as primary id
    global_id = models.IntegerField()

    # The id representing what parent this product belongs to (by parent global_id)
    parent_id = models.IntegerField()
    
    # The local id, only used if the hierarchy level is the lowest
    local_id = models.IntegerField()
    
    # The level of hierarchy this product is in
    level = models.IntegerField()
    
    # an identifier determining if it is a leaf node or aggregate
    identifier = models.CharField(max_length=20)

    # the global id's of the leafs for this product group (if available)
    leaf_children_global = models.CharField(max_length=2000)

    # the local id's of the leafs of this product group (if available)
    leaf_children_local = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Indicator(models.Model):
    # Indicator model to store identifiers for indicators
    
    # The name of the indicator
    name = models.CharField(max_length=200)

    # The product category code
    code = models.CharField(max_length=20, null=True)
    
    # The unit used for the indicator
    unit = models.CharField(max_length=20)
    
    # The global id representing the application coordinates as primary id
    global_id = models.IntegerField()
    
    # The id representing what parent this indicator belongs to (unused as there are no direct summing steps performed for the extensions)
    parent_id = models.IntegerField()
    
    # The local id (unusedas there are no direct summing steps performed for the extensions)
    local_id = models.IntegerField()
    
    # The level of hierarchy this indicator is in
    level = models.IntegerField()

    def __str__(self):
        return self.name
