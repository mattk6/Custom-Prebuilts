from django.contrib import admin

# Register your models here.
from .models import GameSpec, PartsGPU, PartsCPU, Spec


class PartsGPUAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer')
    search_fields = ('id', 'name', 'manufacturer')
    list_filter = ['manufacturer']

class GameSpecAdmin(admin.ModelAdmin):  
    list_display = ('game', 'spec', 'geforce_card_id')

class SpecAdmin(admin.ModelAdmin):
    list_display = ('spec', 'description')

admin.site.register(PartsGPU, PartsGPUAdmin)
admin.site.register(GameSpec, GameSpecAdmin)
admin.site.register(Spec, SpecAdmin)
admin.site.register(PartsCPU)
