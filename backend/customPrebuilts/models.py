"""
models.py
Matthew Kruse
2025-04-13


"""


from django.db import models

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

# Model Name, Manufacturer, Core Count, Core Speed, Socket, Price, Photo (optional)
class PartsCPU(models.Model):
    name = models.CharField(max_length=100)  # CPU Card name
    manufacturer = models.CharField(max_length=50)  # manufacturer
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

# Model Name, Manufacturer, Price, RAM Speed, NVME Slot Count, Ethernet
class PartsMotherboard(models.Model):
    name = models.CharField(max_length=100)  # Motherboard name
    manufacturer = models.CharField(max_length=50)  #  Manufacturer
    msrp = models.FloatField(null=True, blank=True)  # MSRP (nullable)
    nvme_slot_count = models.PositiveIntegerField(null=True, blank=True)  # NVME Slot Count
    ethernet = models.FloatField(null=True, blank=True)  # ethernet speed (nullable)
    photo = models.URLField(max_length=200, null=True, blank=True) # Image / could be url....

    def __str__(self):
        return self.name
