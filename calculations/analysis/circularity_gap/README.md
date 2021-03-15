[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3245310.svg)](https://doi.org/10.5281/zenodo.3245310)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# cgn_supplementary_material

## exio_mr_hiot_v3.3.15_2011
It includes extention accounts from EXIOBASE v.3.3.15 coverted tab-delimited files:
* Resource extraction per economic activity (RE_ACT)
* Resource extraction per final demand category (RE_FD)
* Waste supply per economic activity (WS_ACT)
* Waste supply per final demand category (WS_FD)
* Stock additions per economic activity (SA_ACT)
* Stock additions per final demand category (SA_FD)
* Waste use per economic activity (WU_ACT)
* Stock depletion per final demand category (SD)
* Emissions per economic activity (EM_ACT)
* Emissions per final demand category (EM_FD)
* Population per country (POP)
* GDP-PPP per capita, per country (GDP_CAP_PPP)

**Note**: Intermediate demand matrix (HIOT) is not included in this folder. For running ***cgn_main.py***, HIOT should be downloaded from EXIOBASE website (http://www.exiobase.eu/), and following the import procedure in ***procedure.docx***

## cgn_main.py
Phyton script returns the results of:
* Global circularity gap per material category (data_glo)
* Circularity gap per country (data_cou)
* Circularity gap per aggregated region (data_reg) 

## cgn_sankey.py
Phyton script returns Sankey diagram using floweaver software

**Note**: SankeyWidget performs on Jupyter Notebook 

## results.xls 
Excel file with results from ***cgn_main.py***

## analysis.xls
It includes the circularity gap analysis and figures based on ***results.xlsb*** source data  

## exio_class.xls
It includes from EXIOBASE v.3.3.15:
* List of income groups per counrty based on World Bank Atlas method (https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups)
* Resource extraction classification
* Emission classification
* Waste/stock additions classification
* List of all economic sectors in EXIOBASE
* List of economic activities related to waste recovery in EXIOBASE

## wb_to_exio_cov.xls
Excel file coverts datasets from World Bank Statistics to EXIOBASE classification  

## procedure.docx
Word file contains:
* Procedure to import EXIOBASE v3.3.15, use of 'cgn_main.py', 'cgn_sankey.py', 'results.xls' and 'analysis.xls' 
* A comparison between data from EXIOBASE v3.3.15 and other sources of material flow accounts   
