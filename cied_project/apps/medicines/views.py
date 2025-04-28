from rest_framework import generics
from apps.medicines.models import Medicine
from apps.authentication.permissions import IsInventoryManager
from rest_framework.permissions import IsAuthenticated
from apps.medicines.serializers import MedicineSerializer
from rest_framework.response import Response


# Create your views here.
class MedicineListView(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated, IsInventoryManager]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MedicineCrudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated, IsInventoryManager]

    def get(self, request, *args, **kwargs):
        medicine = self.get_object()
        serializer = self.get_serializer(medicine)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        medicine = self.get_object()
        serializer = self.get_serializer(medicine, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        medicine = self.get_object()
        medicine.delete()
        return Response("Deleted successfully", status=204)
