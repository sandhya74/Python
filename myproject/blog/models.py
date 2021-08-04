from django.db import models
import uuid

class Materials(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    Material_Code = models.CharField(max_length=255,blank=True,null=True)
    Material_Name= models.CharField(max_length=255,blank=True,null=True)
    Material_Location=models.CharField(max_length=255,blank=True,null=True)
    Unit_of_Measurement=models.CharField(max_length=255,null=True, blank=True)  
    Maximum_Level=models.IntegerField(null=True, blank=True)
    Minimum_Level=models.IntegerField(null=True, blank=True)
    Re_order_Level=models.IntegerField(null=True, blank=True)
    Quantity=models.IntegerField(null=True,blank=True)