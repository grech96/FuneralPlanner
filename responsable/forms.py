from .models import Planner
from django import forms

class PlannerForm(forms.ModelForm):

    class Meta: 
        model = Planner

        fields = (
            'ashes',
            'venue',
            'wish',
            'user',
        )    




        