"""
serializers.py
Matthew Kruse
2025-04-13


"""


from rest_framework import serializers
from .models import PartsGPU, PartsCPU, PartsMotherboard, Game, GameSpec, Spec

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

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameSpecSerializer(serializers.ModelSerializer):
    spec_description = serializers.SerializerMethodField()
    game_name = serializers.ReadOnlyField(source='game.name')  # Access the `name` field in the linked `Game` object

    class Meta:
        model = GameSpec
        # put fields in a preferred order
        fields = ['id', 'game', 'game_name', 'spec','spec_description', 'geforce', 'radeon', 'arc', 'fps', 'resolution', 'preset']

    def get_spec_description(self, obj):
        try:
            spec = Spec.objects.get(spec=obj.spec)
            return spec.description
        except Spec.DoesNotExist:
            return None

 