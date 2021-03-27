from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Job

# from django_celery_results import models
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calculations(request):
    """
    Called by the dashboard app for EXIOBASE query
    """
    return HttpResponse("<h1>heeeee</h1>")


