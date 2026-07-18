from django import forms
from .models import Chaia_Variety

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(
        queryset=Chaia_Variety.objects.all(),
        label="Select chai variety",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-gray-700 bg-white appearance-none cursor-pointer'
        })
    )