from django.contrib import admin
from apps.config.models import GrowConfig
class ListGrowConfig(admin.ModelAdmin):
    list_display = ('id', 'stageType', 'watering', 'lastUpdate')
    list_display_links = ('id', 'lastUpdate')
    list_editable = ('stageType', 'watering')
    list_per_page = 1

admin.site.register(GrowConfig, ListGrowConfig)
