from django import forms
from django.forms import ModelForm
from blog.models import *
from blog.views import *

class MaterialsForm(forms.ModelForm):
    import pdb;pdb.set_trace()
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
    
        
    def clean_Material_Code(self):
        import pdb;pdb.set_trace()
        material_code = self.cleaned_data.get['Material_Code']
        for instance in Materials.objects.all():
            if instance.material_code == material_code:
                raise form.ValidationError(Material_Code + 'is already created')
         
        return material_code
      
            		
            



	
