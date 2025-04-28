from django.urls import path
from apps.billing.views import BillingAPIView

urlpatterns = [
    path('billing/', BillingAPIView.as_view(), name='billing_api'),
]