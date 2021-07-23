from rest_framework import serializers
from polls.models import *

class Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Materials
        fields = ( 
        'Material_Code',
        'Material_Descriptions',
        'Material_Location',
        'Unit_of_Measurement',
        'Maximum_Level',
        'Minimum_Level',
        'Re_order_Level')
    def create(self, validated_data):
        return Materials.objects.create(**validated_data)    
