from django.apps import AppConfig


class MaintenanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Maintenance'

    def ready(self):
        from .controllers import MaintenanceController
        MaintenanceController.get_maintenance()
