from rest_framework.views import APIView

from .controllers import MaintenanceController


class MaintenanceList(APIView):
    controller = MaintenanceController

    def get(self, request):
        return self.controller.get_maintenance()

    def update(self, request):
        return self.controller.update_maintenance()

    def delete(self, request):
        return self.controller.delete_maintenance()

    def post(self, request):
        return self.controller.post_maintenance()