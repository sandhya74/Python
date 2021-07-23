from django.shortcuts import render
from polls import serializer
from polls.urls import *
from django.http import HttpResponse, JsonResponse
from polls.models import *
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status 
from rest_framework.decorators import api_view
from polls.serializer import *
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from polls.forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


class Demo(APIView):
    
    def get(self,request):
        
         return render(request,'materialform.html')
       

    def post(self,request):
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
               form.instance.Miniimum_Level = request.POST['minimum_level']
               form.instance.Re_order_Level = request.POST['re_order_level']

               form.save()
            else:
                print(form.errors)
            return HttpResponse(status=200)

    # n


    
    # def post(self,request):
        
    #     serializer=Serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         
    #         self.display(request)
            
    #         return Response(status=200)
    #     else:
    #         print (serializer.errors)
    #         return Response(status=404) 
    #     return render(request, 'materialform.html' )    
    
    # def get(self,request):

    #     var1=Materials.objects.all()
    #     serializer=Serializer(var1,many=True)
    #     return Response(serializer.data , status=200)

    # def put(self, request):

    #     snippet = Materials.objects.get(Material_Id=1001)
    #     serializer = Serializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request):

    #     snippet = Materials.objects.get(Material_Id=1002)
    #     serializer = Serializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         snippet.delete()
    #         return Response(serializer.data)
    #     return Response(status=status.HTTP_204_NO_CONTENT) 

    # def display(self,request):
    #     #import pdb;pdb.set_trace()
    #     snip=Materials.objects.get(Material_Id='1001')
    #     # return render (request,'material.html',{'snip':snip,'form': form,})  
    #     return render (request,'material.html',{'snip':snip})  
    

    #xdef post_form(self,request):
    #     import pdb;pdb.set_trace()
    #     #if request.method == 'POST':

    #     form=MaterialsForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #             #messages.success(request, _('Materials Saved Sucessfully'))
    #         return Response(form.data,status=200)
    #     return Response(forms.errors, status=status.HTTP_400_BAD_REQUEST)

        


# obj=Demo()
# obj.post('POST')            