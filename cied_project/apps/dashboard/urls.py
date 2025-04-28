from django.urls import path
from apps.dashboard.views import StockDetailsAPIView, SalesReportAPIView

urlpatterns = [
    path('stock/', StockDetailsAPIView.as_view(), name='stock_details_api'),
    path('reports/', SalesReportAPIView.as_view(), name='sales_report_api'),
]