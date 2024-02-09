from django.apps import AppConfig


class AppAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppAuth'
    def ready(self) -> None:
        from AppAuth import signals