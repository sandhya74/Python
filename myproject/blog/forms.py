from django import forms
from django.forms import ModelForm
from blog.models import *

class MaterialsForm(forms.ModelForm):
    class Meta:
        model=Materials
        fields = '__all__'