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
    game_name = serializers.ReadOnlyField(source='game.name')
    geforce_fps = serializers.SerializerMethodField()

    class Meta:
        model = GameSpec
        # put fields in a preferred order
        fields = ['id', 'game', 'game_name', 'spec', 'geforce_card_id',
                  'fps', 'resolution', 'preset',
                  'geforce_fps']

    # supply card ratings in the payload
    def get_geforce_fps(self, obj):
        if not obj.geforce_card:
            return None
        return {
            "1080p_medium": obj.geforce_card.fps_1080p_medium,
            "1080p_ultra": obj.geforce_card.fps_1080p_ultra,
            "1440p_ultra": obj.geforce_card.fps_1440p_ultra,
            "4k_ultra": obj.geforce_card.fps_4k_ultra
        }