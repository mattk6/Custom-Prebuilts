"""
serializers.py
Matthew Kruse
2025-04-13


"""


from rest_framework import serializers
from .models import PartsGPU, PartsCPU, PartsMotherboard

class PartsGPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsGPU
        fields = '__all__'

class PartsCPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsCPU
        fields = '__all__'

class PartsMotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsMotherboard
        fields = '__all__'
