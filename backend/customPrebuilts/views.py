"""
views.py
Matthew Kruse
2025-04-17


"""
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import PartsGPU, PartsCPU, PartsMotherboard, Game, GameSpec
from .serializers import PartsGPUSerializer, PartsCPUSerializer, PartsMotherboardSerializer, GameSerializer, GameSpecSerializer

# GPU Views
class PartsGPUViewSet(ReadOnlyModelViewSet):
    queryset = PartsGPU.objects.all()
    serializer_class = PartsGPUSerializer

# CPU Views
class PartsCPUViewSet(ReadOnlyModelViewSet):
    queryset = PartsCPU.objects.all()
    serializer_class = PartsCPUSerializer

# Motherboard Views
class PartsMotherboardViewSet(ReadOnlyModelViewSet):
    queryset = PartsMotherboard.objects.all()
    serializer_class = PartsMotherboardSerializer

# Game Views
class GameViewSet(ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameSpecViewSet(ReadOnlyModelViewSet):
    queryset = GameSpec.objects.all()
    serializer_class = GameSpecSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game__id', 'spec']