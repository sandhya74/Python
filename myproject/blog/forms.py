from django import forms
from django.forms import ModelForm
from blog.models import *
from blog.views import *

class MaterialsForm(forms.ModelForm):
    class Meta:
        model=Materials
        
        fields=( 
            
        'Material_Code',
        'Material_Name',
        'Material_Location',
        'Unit_of_Measurement',
        'Maximum_Level',
        'Minimum_Level',
        'Re_order_Level',
        'Quantity')
    
        
    def clean_material_code(self):
        import pdb;pdb.set_trace()
        material_code = Materials.request.POST['Material_Code']
        if(material_code == ""):
            raise form.ValidationError('This field cannot  be blank')
        for instance in Materials.objects.all():
            if instance.material_code == material_code:
                raise form.ValidationError('This field already created')    
        return material_code
       
        # if material_code == material_code:
        #     raise forms.ValidationError(Material_Code + ' is already created')
        # return material_code
            		
            

