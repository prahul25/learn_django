from django import forms
from .models import Chaia_Variety

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=Chaia_Variety.objects.all(), label="Select chai variety")