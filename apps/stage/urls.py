from django.urls import path
from apps.stage.views import show, list

urlpatterns = [
    path('', list, name='stageList'),
    path('show', show, name='stageShow'),
]
