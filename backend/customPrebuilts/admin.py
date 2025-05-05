from django.contrib import admin
from django.db import models

# Register your models here.
from .models import GameSpec, PartsCPU, Spec, PartsGPU

class PartsGPUAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer')
    search_fields = ('id', 'name', 'manufacturer')
    list_filter = ['manufacturer']

class GameSpecAdmin(admin.ModelAdmin):
    list_display = ('game', 'spec', 'geforce_card_id')

    # establish drop down sorting on gpu name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "geforce_card":
            kwargs["queryset"] = PartsGPU.objects.order_by("name")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SpecAdmin(admin.ModelAdmin):
    list_display = ('spec', 'description')

admin.site.register(PartsGPU, PartsGPUAdmin)
admin.site.register(GameSpec, GameSpecAdmin)
admin.site.register(Spec, SpecAdmin)