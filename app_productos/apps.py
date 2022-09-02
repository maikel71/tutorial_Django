from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class AppProductosConfig(AppConfig):
    name = 'app_productos'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
