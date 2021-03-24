from django import forms
from .models import ScenarioChanges

class ScenarioForm(forms.ModelForm):
    class  Meta:
        model = ScenarioChanges
        fields = [
            'source1',
            'value',
            'target1'
        ]