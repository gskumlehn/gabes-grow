from django import forms
from apps.config.models import GrowConfig

class ConfigForm(forms.ModelForm):
    class Meta:
        model = GrowConfig
        exclude = ['lastUpdate']
        widgets = {
            "stageType": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "lastUpdate": forms.HiddenInput(
                attrs={
                    "class": "form-control",
                }
            )
        }
