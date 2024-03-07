from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_user_model_extending.accounts"

    def ready(self):
        import django_user_model_extending.accounts.signals