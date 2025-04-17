from django.contrib import admin

# Register your models here.
from .models import GameSpec, PartsGPU, PartsCPU, Spec


class PartsGPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'year')
    search_fields = ('name', 'manufacturer', 'year')
    list_filter = ('manufacturer','year')

class GameSpecAdmin(admin.ModelAdmin):  
    list_display = ('game', 'spec')

class SpecAdmin(admin.ModelAdmin):
    list_display = ('spec', 'description')

admin.site.register(PartsGPU, PartsGPUAdmin)
admin.site.register(GameSpec, GameSpecAdmin)
admin.site.register(Spec, SpecAdmin)
admin.site.register(PartsCPU)

