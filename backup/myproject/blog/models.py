from django.db import models
import uuid

class Materials(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    Material_Code = models.CharField(max_length=255,blank=True,null=True)
    Material_Descriptions = models.CharField(max_length=255,blank=True,null=True)
    Material_Location=models.CharField(max_length=255,blank=True,null=True)
    Unit_of_Measurement=models.CharField(max_length=255,null=True, blank=True, default=0)  
    Maximum_Level=models.IntegerField(null=True, blank=True, default=0)
    Minimum_Level=models.IntegerField(null=True, blank=True, default=0)
    Re_order_Level=models.IntegerField(null=True, blank=True, default=0)