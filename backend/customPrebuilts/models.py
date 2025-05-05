"""
models.py
Matthew Kruse
2025-04-13


"""
from django.db import models

# list of games from steam store
class Game(models.Model):
    steam_store_id = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# game play specification, e.g. 1 = minimum, 2 = recommended
class Spec(models.Model):
    spec = models.IntegerField(unique=True)
    description = models.CharField(max_length=20)

# list of gpu models and their specs
class PartsGPU(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    msrp = models.FloatField(null=True, blank=True)
    photo = models.URLField(max_length=200, null=True, blank=True)
    fps_1080p_medium = models.FloatField(null=True, blank=True)
    fps_1080p_ultra = models.FloatField(null=True, blank=True)
    fps_1440p_ultra = models.FloatField(null=True, blank=True)
    fps_4k_ultra = models.FloatField(null=True, blank=True)
    gpu_chip_model = models.CharField(max_length=50)
    cuda_cores = models.PositiveIntegerField()
    boost_clock = models.PositiveIntegerField()
    memory = models.CharField(max_length=50)
    memory_bandwidth = models.PositiveIntegerField()
    power_consumption = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(name='unique_gpus',
                fields=['name', 'manufacturer', 'cuda_cores', 'memory'])
        ]

    def __str__(self):
        return self.name

# list of cpu models and their specs
class PartsCPU(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    series = models.CharField(max_length=50, blank=True)
    msrp = models.FloatField(null=True, blank=True)
    core_count = models.PositiveIntegerField()
    core_speed = models.FloatField(null=True, blank=True)
    boost_speed = models.FloatField(null=True, blank=True)
    socket = models.CharField(max_length=50)
    photo = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(name='unique_cpus',
                fields=['name', 'manufacturer', 'core_count', 'core_speed', 'socket', 'photo'])
        ]

    def __str__(self):
        return self.name

# list of motherboards and their specs
class PartsMotherboard(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    msrp = models.FloatField(null=True, blank=True)
    nvme_slot_count = models.PositiveIntegerField(null=True, blank=True)
    ethernet = models.FloatField(null=True, blank=True)
    photo = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

# specification for game hardware requirement based on Spec
class GameSpec(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    spec = models.IntegerField()
    geforce_card = models.ForeignKey(PartsGPU, on_delete=models.SET_NULL, null=True, blank=True)
    fps = models.IntegerField(blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    preset = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.game.name
