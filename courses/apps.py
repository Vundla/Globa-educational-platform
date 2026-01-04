from django.apps import AppConfig


class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
    
    def ready(self):
        """Import signal handlers when app is ready - enables Apache signal support"""
        import courses.signals
