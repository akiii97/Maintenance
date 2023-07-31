from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Maintenance
from .serializers import MaintenanceSerializers


class MaintenanceController(APIView):

    @classmethod
    def get_maintenance(cls, ):
        maintenance = Maintenance.objects.all()
        serializers = MaintenanceSerializers(maintenance, many=True)
        return Response(serializers.data)

    @classmethod
    def update_maintenance(cls, request):
        update_id = request.data.get('id')
        try:
            maintenance = Maintenance.objects.filter(id=update_id)
        except Maintenance.DoesNotExist:
            return Response("Maintenance not found", status=status.HTTP_404_NOT_FOUND)
        serializer = MaintenanceSerializers(maintenance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @classmethod
    def post_maintenance(cls, request):
        serializer = MaintenanceSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def delete_maintenance(cls, request):
        maintenance_id = request.data.get('id')
        maintenance = Maintenance.objects.get(id=maintenance_id)
        maintenance.delete()
        return Response("Deleted Successfully ")

