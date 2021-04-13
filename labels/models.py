from django.db import models

# Create your models here.



class Region(models.Model):
    """
    Country model to store identifiers for the countries and aggregations
    """
    name = models.CharField(max_length=200)
    """
    The name of the country
    """
    code = models.CharField(max_length=200)
    """
    The country code
    """
    global_id = models.IntegerField()
    """
    The global id representing the application coordinates as primary id
    """
    parent_id = models.IntegerField()
    """
    The id representing what parent this country belongs to (by parent global_id)
    """
    local_id = models.IntegerField()
    """
    The local id, only used if the hierarchy level is the lowest
    """
    level = models.IntegerField()
    """
    The level of hierarchy this country is in
    """
    identifier = models.CharField(max_length=200)
    """
    an identifier determining if it is a leaf node or aggregate
    """
    leaf_children_global = models.TextField(max_length=1000)
    """
    the global id's of the leafs for this continent (if available)
    """
    leaf_children_local = models.TextField(max_length=1000)
    """
    the local id's of the leafs of this country (if available)
    """

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model to store identifiers for the products and aggregations
    """
    name = models.CharField(max_length=200)
    """
        The name of the product category
    """
    code = models.CharField(max_length=200)
    """
        The product category code
    """
    global_id = models.IntegerField()
    """
        The global id representing the application coordinates as primary id
    """
    parent_id = models.IntegerField()
    """
        The id representing what parent this product belongs to (by parent global_id)
    """
    local_id = models.IntegerField()
    """
        The local id, only used if the hierarchy level is the lowest
    """
    level = models.IntegerField()
    """
       The level of hierarchy this product is in
    """
    identifier = models.CharField(max_length=200)
    """
        an identifier determining if it is a leaf node or aggregate
     """
    leaf_children_global = models.TextField(max_length=1000)
    """
        the global id's of the leafs for this product group (if available)
    """
    leaf_children_local = models.TextField(max_length=1000)
    """
        the local id's of the leafs of this product group (if available)
    """

    def __str__(self):
        return self.name

class Activity(models.Model):
    """
    Product model to store identifiers for the products and aggregations
    """
    name = models.CharField(max_length=200)
    """
        The name of the product category
    """
    code = models.CharField(max_length=200)
    """
        The product category code
    """
    global_id = models.IntegerField()
    """
        The global id representing the application coordinates as primary id
    """
    parent_id = models.IntegerField()
    """
        The id representing what parent this product belongs to (by parent global_id)
    """
    local_id = models.IntegerField()
    """
        The local id, only used if the hierarchy level is the lowest
    """
    level = models.IntegerField()
    """
       The level of hierarchy this product is in
    """
    identifier = models.CharField(max_length=200)
    """
        an identifier determining if it is a leaf node or aggregate
     """
    leaf_children_global = models.TextField(max_length=1000)
    """
        the global id's of the leafs for this product group (if available)
    """
    leaf_children_local = models.TextField(max_length=1000)
    """
        the local id's of the leafs of this product group (if available)
    """

    def __str__(self):
        return self.name


class FinaldDemand(models.Model):
    """
    Modelling data-model to store identifiers for the products and aggregations (slight modified version of Product)
    """
    name = models.CharField(max_length=200)
    """
        The name of the product category
    """
    code = models.CharField(max_length=200)
    """
        The product category code
    """
    global_id = models.IntegerField()
    """
        The global id representing the application coordinates as primary id
    """
    parent_id = models.IntegerField()
    """
        The id representing what parent this product belongs to (by parent global_id)
    """
    local_id = models.IntegerField()
    """
        The local id, only used if the hierarchy level is the lowest
    """
    level = models.IntegerField()
    """
       The level of hierarchy this product is in
    """
    identifier = models.CharField(max_length=200)
    """
        an identifier determining if it is a leaf node or aggregate
     """
    leaf_children_global = models.TextField(max_length=1000)
    """
        the global id's of the leafs for this product group (if available)
    """
    leaf_children_local = models.TextField(max_length=1000)
    """
        the local id's of the leafs of this product group (if available)
    """

    def __str__(self):
        return self.name


class Indicator(models.Model):
    """
    Indicator model to store identifiers for indicators
    """
    name = models.CharField(max_length=200)
    """
        The name of the indicator
    """
    unit = models.CharField(max_length=200)
    """
        The unit used for the indicator
    """
    global_id = models.IntegerField()
    """
        The global id representing the application coordinates as primary id
    """
    parent_id = models.IntegerField()
    """
        The id representing what parent this indicator belongs to (unused as there are no direct summing steps performed for the extensions)
    """
    local_id = models.IntegerField()
    """
        The local id (unusedas there are no direct summing steps performed for the extensions)
    """
    level = models.IntegerField()
    """
        The level of hierarchy this indicator is in
    """

    def __str__(self):
        return self.name
