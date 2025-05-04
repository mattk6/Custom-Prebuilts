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


    def get_geforce_fps(self, obj):
        return self.get_gpu_fps(obj.geforce_card_id)

    def get_gpu_fps(self, gpu_id):
        try:
            gpu = PartsGPU.objects.get(id=gpu_id)
            return {
                "1080p_medium": gpu.fps_1080p_medium,
                "1080p_ultra": gpu.fps_1080p_ultra,
                "1440p_ultra": gpu.fps_1440p_ultra,
                "4k_ultra": gpu.fps_4k_ultra
            }
        except PartsGPU.DoesNotExist:
            return None        

 