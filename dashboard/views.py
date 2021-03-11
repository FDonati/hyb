from django.shortcuts import render
from django.http import HttpResponse
from .models import SupplyChain

from .forms import  ScenarioForm

# Create your views here.

def scenario_create_view(request, *args, **kwargs):

    form = ScenarioForm(request.POST or None)
    
    if form.is_valid():
        form.save()
    context = {
        "form" : form
    }
 
    return context



def dashboard_view(request, *args, **kwargs):

    obj =  SupplyChain.objects.get(id=1)
    context = {
        "object" : obj,
        "form" : scenario_create_view(request)["form"]
    }
    return render(request, "dashboard.html", context)
