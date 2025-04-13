"""
views.py
Matthew Kruse
2025-04-13


"""


from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import PartsGPU, PartsCPU, PartsMotherboard
from .serializers import PartsGPUSerializer, PartsCPUSerializer, PartsMotherboardSerializer

# GPU Views
class PartsGPUListCreateView(ModelViewSet):
    queryset = PartsGPU.objects.all()
    serializer_class = PartsGPUSerializer

class PartsGPURetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartsGPU.objects.all()
    serializer_class = PartsGPUSerializer

# CPU Views
class PartsCPUListCreateView(ModelViewSet):
    queryset = PartsCPU.objects.all()
    serializer_class = PartsCPUSerializer

class PartsCPURetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartsCPU.objects.all()
    serializer_class = PartsCPUSerializer

# Motherboard Views
class PartsMotherboardListCreateView(ModelViewSet):
    queryset = PartsMotherboard.objects.all()
    serializer_class = PartsMotherboardSerializer

class PartsMotherboardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartsMotherboard.objects.all()
    serializer_class = PartsMotherboardSerializer
