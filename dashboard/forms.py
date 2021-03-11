from django import forms
from .models import SupplyChain

class ScenarioForm(forms.ModelForm):
    class  Meta:
        model = SupplyChain
        fields = [
            'source1',
            'value',
            'target1'
        ]