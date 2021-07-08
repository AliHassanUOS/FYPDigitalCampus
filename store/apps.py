from django.apps import AppConfig
from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'

    def ready(self):
        from . import mysignal




