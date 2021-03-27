from django import forms
from .models import ScenarioChange

class ScenarioForm(forms.ModelForm):
    class  Meta:
        model = ScenarioChange
        fields = [
            'source1',
            'value',
            'target1'
        ]