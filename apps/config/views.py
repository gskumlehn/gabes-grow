from apps.config.forms import ConfigForm
from apps.config.models import GrowConfig
from apps.config.functions.Lights import *
from django.contrib import messages
from django.shortcuts import render, redirect
from apps.config.functions.Watering import waterIfDryAndWateringOn

def index(request, config_id):
    config = GrowConfig.objects.get(id=config_id)
    form = ConfigForm(instance=config)
    return render(request, 'config/show.html', {"config": config, "form": form})

def edit(request, config_id):
    config = GrowConfig.objects.get(id=config_id)
    form = ConfigForm(request.POST, instance=config)

    if form.is_valid():
        updatedConfig = form.save()
        if updatedConfig.lights:
            lightsOn()
        else:
            lightsOff()
        messages.success(request, "Config updated")
    else:
        messages.error(request, "Config update failed")

    return redirect('config', config_id=config_id)

def water(request):
    waterIfDryAndWateringOn()

    return redirect('index')