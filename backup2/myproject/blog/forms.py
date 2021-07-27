from django import forms
from django.forms import ModelForm
from blog.models import *

class MaterialsForm(forms.ModelForm):
    class Meta:
        model=Materials
        
        fields=( 
            
        'Material_Code',
        'Material_Descriptions',
        'Material_Location',
        'Unit_of_Measurement',
        'Maximum_Level',
        'Minimum_Level',
        'Re_order_Level')