from rest_framework import generics
from rest_framework.response import Response
from apps.billing.serializers import BillingSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.authentication.permissions import IsStaff
# Create your views here.

class BillingAPIView(generics.CreateAPIView):
    """
    API view to handle billing operations.
    """
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated, IsStaff]

    def create(self, request, *args, **kwargs):
        """
        Create a new billing record.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)