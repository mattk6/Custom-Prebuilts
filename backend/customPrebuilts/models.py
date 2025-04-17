"""
models.py
Matthew Kruse
2025-04-13


"""


from django.db import models


# list of games from steam store
class Game(models.Model):
    steam_store_id = models.IntegerField() # Steam Store ID
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# specification for game hardware requirement based on Spec
class GameSpec(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    spec = models.IntegerField()
    geforce = models.CharField(max_length=50, blank=True)
    radeon = models.CharField(max_length=50, blank=True)
    arc = models.CharField(max_length=50, blank=True)
    fps = models.IntegerField(blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    preset = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.game.name

# game play specification, e.g. 1 = minimum, 2 = recommended
class Spec(models.Model):
    spec = models.IntegerField(unique=True)
    description = models.CharField(max_length=20)
 

class PartsGPU(models.Model):
    name = models.CharField(max_length=100)  # Graphics Card name
    manufacturer = models.CharField(max_length=50)  # manufacturer
    msrp = models.FloatField(null=True, blank=True)  # MSRP
    photo = models.URLField(max_length=200, null=True, blank=True) # Image / could be url....
    year = models.IntegerField(null=True, blank=True)  # Year of release
    fps_1080p_medium = models.CharField(max_length=50, null=True, blank=True)  # 1080p Medium FPS
    fps_1080p_ultra = models.CharField(max_length=50, null=True, blank=True)  # 1080p Ultra FPS
    fps_1440p_ultra = models.CharField(max_length=50, null=True, blank=True)  # 1440p Ultra FPS
    fps_4k_ultra = models.CharField(max_length=50, null=True, blank=True)  # 4K Ultra FPS
    gpu_chip_model = models.CharField(max_length=50)  # GPU chip model
    cuda_cores = models.PositiveIntegerField()  # Number of CUDA cores
    boost_clock = models.PositiveIntegerField()  # Boost clock in MHz
    memory = models.CharField(max_length=50)  # Memory type and size (e.g., "24GB GDDR6X")
    memory_bandwidth = models.PositiveIntegerField()  # Bandwidth in GB/s
    power_consumption = models.PositiveIntegerField()  # Power consumption in watts

    class Meta:
        unique_together = ('name', 'manufacturer', 'year', 'cuda_cores', 'memory')

    def __str__(self):
        return self.name

# list of cpu models and their specs
class PartsCPU(models.Model):
    name = models.CharField(max_length=100)  # CPU Card name
    manufacturer = models.CharField(max_length=50)  # manufacturer
    series = models.CharField(max_length=50)  # Series
    msrp = models.FloatField(null=True, blank=True)  # MSRP
    core_count = models.PositiveIntegerField()  # Core count
    core_speed = models.FloatField(null=True, blank=True)  # core speed
    boost_speed = models.FloatField(null=True, blank=True)  # boost speed
    socket = models.CharField(max_length=50)  # String
    photo = models.URLField(max_length=200, null=True, blank=True) # Image / could be url....

    class Meta:
        unique_together = ('name', 'manufacturer', 'core_count', 'core_speed', 'socket', 'photo')

    def __str__(self):
        return self.name

# list of motherboard models and their specs
class PartsMotherboard(models.Model):
    name = models.CharField(max_length=100)  # Motherboard name
    manufacturer = models.CharField(max_length=50)  #  Manufacturer
    msrp = models.FloatField(null=True, blank=True)  # MSRP (nullable)
    nvme_slot_count = models.PositiveIntegerField(null=True, blank=True)  # NVME Slot Count
    ethernet = models.FloatField(null=True, blank=True)  # ethernet speed (nullable)
    photo = models.URLField(max_length=200, null=True, blank=True) # Image / could be url....

    def __str__(self):
        return self.name
