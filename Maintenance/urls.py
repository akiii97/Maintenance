from django.urls import path
from .views import MaintenanceList

app_name = 'Maintenance'

urlpatterns = [
    path("", MaintenanceList.as_view(), name='Maintenance-list'),
]
