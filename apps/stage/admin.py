from django.contrib import admin
from apps.stage.models import Stage

class ListStage(admin.ModelAdmin):
    list_display = ('type', 'lightOn', 'lightOff', 'phMin', 'phMax', 'tempMin', 'tempMax', 'soilHumMin', 'soilHumMax', 'airHumMin', 'airHumMax',)
    list_display_links = ('type', 'lightOn', 'lightOff', 'phMin', 'phMax', 'tempMin', 'tempMax', 'soilHumMin', 'soilHumMax', 'airHumMin', 'airHumMax',)
    list_per_page = 5

admin.site.register(Stage, ListStage)
