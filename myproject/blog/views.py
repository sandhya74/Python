from django.shortcuts import render, redirect
from blog.models import *
from blog.forms import *
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponseRedirect('/master_page')


def material_List(request):  
    #import pdb;pdb.set_trace()
    material= Materials.objects.all()  
    return render(request,"material_list.html",{'material':material})  
def master_Page(request):
    material=Materials.objects.all()
    return render(request,"master_page.html",{'material':material})    

def create_Material(request): 
    import pdb;pdb.set_trace()
      
    if request.method == "POST":
        form = MaterialsForm(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            form.instance.Material_Code = request.POST['Material_Code']
            form.instance.Material_Descriptions = request.POST['Material_Name']
            form.instance.Material_Location = request.POST['Material_Location']
            form.instance.Unit_of_Measurement = request.POST['Unit_of_Measurement']
            form.instance.Maximum_Level = request.POST['Maximum_Level']
            form.instance.Minimum_Level = request.POST['Minimum_Level']
            form.instance.Re_order_Level = request.POST['Re_order_Level']
            form.instance.Quantity=request.POST['Quantity']
            #form = MaterialsForm.clean_material_code('Material_Code')
           
            form.save()
                #import pdb;pdb.set_trace()
            return HttpResponseRedirect('/material_list')
        
        else:
            print(form.errors)
    else:
        form = MaterialsForm()
        return render(request,'create_material.html',{'form':form})  

def material_Update(request,id):  
    import pdb;pdb.set_trace()
    material = Materials.objects.get(id=id)
    
    form = MaterialsForm(initial={'Material_Code':material.Material_Code, 'Material_Name': material.Material_Name
    , 
    'Material_Location': material.Material_Location, 'Unit_of_Measurement': material.Unit_of_Measurement,'Maximum_Level':material.Maximum_Level,
    'Minimum_Level':material.Minimum_Level,'Re_order_Level':material.Re_order_Level,'Quantity':material.Quantity})
    
    if request.method == "POST":  
        form = MaterialsForm(request.POST,instance=material)  
        
        if form.is_valid():  
            try:  
                form.save() 
                #model = form.instance
                return HttpResponseRedirect('/material_list')  
            except Exception as e: 
                return Response(status=404)   
    
    else:  
        import pdb;pdb.set_trace()     
        return render(request,'create_material.html',{'form':form,'mat_id':material.id,'material':material}) 
        #return render(request,'material_update.html',{'form':form})  

# def material_Delete(request,id):
#     #import pdb;pdb.set_trace()
#     material= Materials.objects.get(id=id)
    
#     try:
#         material.delete()
#         return HttpResponseRedirect('/material_list')
#     except:
#         return Response(status=404) 

def cancel(request):
    return HttpResponseRedirect('/material_list')
    

    