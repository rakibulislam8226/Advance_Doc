from django.apps import AppConfig


class LearnSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learn_signals'
    
    def ready(self):
        import learn_signals.signals
