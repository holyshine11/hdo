from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'MOILST', 'MOJUSO1', 'MAPS_X', 'MAPS_Y', 'UJONG', 'SMART', 'PRICE']
        
    def create(self, validated_data):
        return Station.objects.create(**validated_data)
