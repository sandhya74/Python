from django.shortcuts import render
from blog import serializer
from blog.urls import *
from django.http import HttpResponse, JsonResponse
from blog.models import *
import requests 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status 
from rest_framework.decorators import api_view
from blog.serializer import *

class Demo(APIView):
    
    
    def post(self,request):
        
        serializer=Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            print (serializer.errors)
            return Response(status=406) 
    
    def get(self,request):
        var1=Materials.objects.all()
        serializer=Serializer(var1,many=True)
        return Response(serializer.data , status=200)

    def put(self, request):
        snippet = Materials.objects.get(Material_Id=1001)
        serializer = Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        snippet = Materials.objects.get(Material_Id=1002)
        serializer = Serializer(snippet, data=request.data)
        if serializer.is_valid():
            snippet.delete()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)        

# obj=Demo()
# obj.post('POST')            