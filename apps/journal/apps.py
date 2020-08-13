from django.apps import AppConfig


class JournalConfig(AppConfig):
    name = 'apps.journal'
    verbose_name = 'Journal'

    def ready(self):
        import apps.journal.signals
