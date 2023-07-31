from rest_framework import  serializers
from .models import Maintenance


class MaintenanceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Maintenance
        fields = '__all__'
