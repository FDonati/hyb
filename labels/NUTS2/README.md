# NUTS2_EXIOBASE

This repository contains script to retrieve a diverse set of data to disaggreagate Exiobase at the NUTS2 level. 
It also merges regional labels for NUTS2 and EXIOBASE and products, gnerates the tree-labels to be used in RAMA-SCENE, CIRCUMAT and Hyb projects

The work was mostly developed by Sidney Niccolson. This is an adaptation from his work that was first integrated directly into the webapplications. 

I am now separating from the original web application to clarify structure and allow to repurpose it for other applications more easily. 

## NUTS2_exio_labels

### create_hierarchy_country.py
Prepare a CSV for hierarchical tree structures related to NUTS2 for CircuMat
Usage:
    The file reads in two files, one is a NUTS file containing all nuts classifications
    ,the other file contains EXIOBASE classifications. Country codes are used to match countries with NUTS.
    Nuts2 are filtered by using character count (2-letter countrycode + 2 digit numbers for nuts2).
    Note1: United kingdom is originally with 2-letter code GB in DESIRE/EXIOBASE, this is modified in the EXIOBASE classification
    Note2: Greece is named GR but EL in NUTS2 this is also modified.
    Note3: Iceland (IS), Montenegro (ME), Macedonia (MK), Liechtenstein (LI) are not represented in EXIOBASE
    Note4: Turkey is excluded

### prepare_csv.py
Prepare a CSV from original Tree Raw Data.
        It contains additional fields useful for optimized use in Django Database and EXIOBASE
        Fields:
            "Identifier" -> to identify if Root, Aggregation or Leaf
            "leaf_children_global" -> the leafs that belong to a given node represented in global_ids
            "leaf_children_local" -> the leafs that belong to a given node represented in EXIOBASE indices
        MAX-DEPTH/hierarchies: 4 levels for this script
Usage: change path of MY_TREE_FILE to the country or product files

### prepare_modelling_csv.py
Purpose: Modify the product csv made from prepare_csv.py for use as a tree in modelling view.
        It create to files: prefix=modelling_mod for DB use and prefix=modelling_ for front-end use
        MAX_NUMBER_OF_GLOBAL_IDS and MAX_NUMBER_OF_LOCAL_IDS refers to the product.csv made from prepare_csv
        Check header for which column it refers to
Usage: if the mod_final_productTree.csv is available you can run the script. Please check the MAX_ if there are any changes


# More info
For more information see:
-  https://github.com/SidneyNiccolson/IEplatform/tree/master/IEMasterProject
-  https://github.com/CMLPlatform/ramascene/tree/master/python_ini
-  https://github.com/CMLPlatform/CircuMAT/tree/master/python_ini