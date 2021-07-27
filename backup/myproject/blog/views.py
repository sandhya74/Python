from django.shortcuts import render, redirect
from blog.models import *
from blog.forms import *

# Create your views here.
def material_List(request):  
    import pdb;pdb.set_trace()
    material= Materials.objects.all()  
    return render(request,"material_list.html",{'material':material})  

def create_Material(request): 
    import pdb;pdb.set_trace()
       
    if request.method == "POST":
        form = MaterialsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.instance.Material_Code = request.POST['material_code']
            form.instance.Material_Descriptions = request.POST['material_descriptions']
            form.instance.Material_Location = request.POST['material_location']
            form.instance.Unit_of_Measurement = request.POST['unit_of_measurement']
            form.instance.Maximum_Level = request.POST['maximum_level']
            form.instance.Miniimum_Level = int(request.POST['minimum_level'])
            form.instance.Re_order_Level = request.POST['re_order_level']

            form.save()
            #return redirect('/material')
        else:
            print(form.errors)
   
    return render(request,'create_material.html')  

def material_Update(request,id):  
    import pdb;pdb.set_trace()
    material = Materials.objects.get(id=id)
    form = MaterialsForm(initial={'material_code':materials.Material_Code, 'material_descriptions': materials.Material_Descriptions, 
    'material_location': materials.Material_Location, 'unit_of_measurement': materials.Unit_of_Measurement,'maximum_level':materials.Maximum_Level,
    'minimum_level':materials.Minimum_Level,'re_order_level':materials.Re_order_Level})
    if request.method == "POST":  
        form = MaterialsForm(request.POST, instance=material)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                #return redirect('/book-list')  
            except Exception as e: 
                pass    
    return render(request,'material_update.html',{'form':form})  

def material_Delete(request, id):
    material= Materials.objects.get(id=id)
    try:
        material.delete()
    except:
        pass
    #return redirect('book-list')