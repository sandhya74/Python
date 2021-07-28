from django.shortcuts import render, redirect
from blog.models import *
from blog.forms import *
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponseRedirect('/material_list')


def material_List(request):  
    #import pdb;pdb.set_trace()
    material= Materials.objects.all()  
    return render(request,"material_list.html",{'material':material})  

def create_Material(request): 
    #import pdb;pdb.set_trace()
       
    if request.method == "POST":
        form = MaterialsForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            form.instance.Material_Code = request.POST['material_code']
            form.instance.Material_Descriptions = request.POST['material_descriptions']
            form.instance.Material_Location = request.POST['material_location']
            form.instance.Unit_of_Measurement = request.POST['unit_of_measurement']
            form.instance.Maximum_Level = request.POST['maximum_level']
            form.instance.Minimum_Level = request.POST['minimum_level']
            form.instance.Re_order_Level = request.POST['re_order_level']
            form.save()
            #import pdb;pdb.set_trace()
            return HttpResponseRedirect('/material_list')
        
        else:
            print(form.errors)
    else:
        return render(request,'create_material.html')  

def material_Update(request,id):  
    #import pdb;pdb.set_trace()
    material = Materials.objects.get(id=id)
    
    form = MaterialsForm(initial={'Material_Code':material.Material_Code, 'Material_Descriptions': material.Material_Descriptions, 
    'Material_Location': material.Material_Location, 'Unit_of_Measurement': material.Unit_of_Measurement,'Maximum_Level':material.Maximum_Level,
    'Minimum_Level':material.Minimum_Level,'Re_order_Level':material.Re_order_Level})
    
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
        return render(request,'material_update.html',{'form':form})  

def material_Delete(request,id):
    #import pdb;pdb.set_trace()
    material= Materials.objects.get(id=id)
    
    try:
        material.delete()
        return HttpResponseRedirect('/material_list')
    except:
        return Response(status=404) 

def cancel(request):
    return HttpResponseRedirect('/material_list')
    

    