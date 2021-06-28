from django.db import models
import uuid

class Materials(models.Model):
    Material_Id=models.UUIDField(primary_key=True)
    Material_Code = models.CharField(max_length=255,blank=True,null=True)
    Material_Descriptions = models.CharField(max_length=255,blank=True,null=True)
    Material_Location=models.CharField(max_length=255,blank=True,null=True)
    Unit_of_Measurement=models.IntegerField(null=True, blank=True, default=0)
    Maximum_Level=models.IntegerField(null=True, blank=True, default=0)
    Minimum_Level=models.IntegerField(null=True, blank=True, default=0)
    Re_order_Level=models.IntegerField(null=True, blank=True, default=0)
    # class Meta:
    #     dp_table="blog_materials"