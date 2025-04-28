from rest_framework import generics
from rest_framework.response import Response
from apps.medicines.models import Medicine
from apps.authentication.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from apps.dashboard.serializers import MedicineStockSerializer

# Create your views here.
class StockDetailsAPIView(generics.ListAPIView):
    """
    API view to handle stock details operations.
    """
    queryset = Medicine.objects.all()
    serializer_class = MedicineStockSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    