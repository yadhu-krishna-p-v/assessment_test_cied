from django.shortcuts import render
from rest_framework import generics
from apps.medicines.models import Medicine
from apps.authentication.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from apps.medicines.serializers import MedicineSerializer

# Create your views here.
class StockDetailsAPIView(generics.ListAPIView):
    """
    API view to handle stock details operations.
    """
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    