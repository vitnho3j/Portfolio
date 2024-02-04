from django.apps import AppConfig


class AplicationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aplication"

    def ready(self):
        import aplication.signals