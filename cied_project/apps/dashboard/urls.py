from django.urls import path
from apps.dashboard.views import StockDetailsAPIView

urlpatterns = [
    path('stock/', StockDetailsAPIView.as_view(), name='stock_details_api'),
]