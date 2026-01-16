from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    # # registering signals.py to auto save user profile when account is created
    def ready(self):
        import accounts.signals
