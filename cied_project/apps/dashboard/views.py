from rest_framework import generics
from rest_framework.response import Response
from apps.medicines.models import Medicine
from apps.authentication.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from apps.dashboard.serializers import MedicineStockSerializer
from apps.billing.serializers import BillSerializer
from apps.billing.models import Bill

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
        from django.db import models
        queryset = self.get_queryset()
        overall_sales = queryset.aggregate(
            total_revenue=Sum('total_amount'),
            total_bills=Count('id')
        )
        average_bill_value = overall_sales['total_revenue'] / overall_sales['total_bills'] if overall_sales['total_bills'] else 0
        staff_sales = queryset.values('staff').annotate(
            staff_name=models.F('staff__username'),
            bills_count=Count('id'),
            revenue_generated=Sum('total_amount')
        ).order_by('-revenue_generated')
        response_data = {
            "overall_sales": {
                "total_revenue": overall_sales['total_revenue'] or 0,
                "total_bills": overall_sales['total_bills'] or 0,
                "average_bill_value": average_bill_value
            },
            "staff_sales": list(staff_sales),
        }

        return Response(response_data)