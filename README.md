# Hyb
---
Hyb is a django 3.1.7 based web-application that allows for analyzing Environmentally Extended Hybrid Input-Output (EEIO) tables. EXIOBASE v3 is used in this project. 
Demo version: NOT AVAILABLE YET

The Hyb project develops on the experience acquired through the EU Commission funded projects RaMa-Scene, Circumat and CircEUit.  

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](resources/docs/CONTRIBUTING.md)

# Developers Guide
---
NOT AVAILABLE YET

# Getting started
---

### Retrieve the raw datasets

NOT AVAILABLE YET

### Clone the project 
``` 
git clone https://github.com/FDonati/hyb.git

``` 
### Install docker
https://docs.docker.com/compose/install/

## Run the project

In the directory where you cloned the project run
the following commands

### Prepare the database
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
### start the container
```
$ docker-compose up
```

