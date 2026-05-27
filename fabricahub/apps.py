from django.apps import AppConfig


class FabricahubConfig(AppConfig):
    name = 'fabricahub'

    def ready(self):
        import fabricahub.signals