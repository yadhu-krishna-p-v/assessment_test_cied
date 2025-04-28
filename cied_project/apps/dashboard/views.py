from rest_framework import generics
from rest_framework.response import Response
from apps.medicines.models import Medicine
from apps.authentication.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from apps.dashboard.serializers import MedicineStockSerializer
from apps.billing.serializers import BillSerializer

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
    
    
class SalesReportAPIView(generics.ListAPIView):
    """
    API view to handle sales report operations.
    """
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def get_queryset(self):
        queryset = Bill.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        staff_id = self.request.query_params.get('staff_id')
        if start_date:
            queryset = queryset.filter(created_at__date__gte=start_date)
        if end_date:
            queryset = queryset.filter(created_at__date__lte=end_date)
        if staff_id:
            queryset = queryset.filter(staff_id=staff_id)
        return queryset
    
    def list(self, request, *args, **kwargs):
        from django.db.models import Sum, Count
        queryset = self.get_queryset()
        overall_sales = queryset.aggregate(
            total_revenue=Sum('total_amount'),
            total_bills=Count('id')
        )