from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.profiles"

    def ready(self):
        from api.profiles import signals
