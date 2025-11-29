from rest_framework import serializers
from .models import*


class SensorData_Serializers(serializers.ModelSerializer):
    class Meta:
        model=SensorData
        fields=['id','temperature','humidity','co2','noise','light','color','timestamp']