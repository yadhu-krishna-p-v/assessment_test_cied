from rest_framework import generics
from rest_framework.response import Response
from apps.billing.serializers import BillSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.authentication.permissions import IsStaff
from apps.billing.models import Bill, BillItem
from apps.medicines.models import Medicine
# Create your views here.

class BillingAPIView(generics.CreateAPIView):
    """
    API view to handle billing operations.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated, IsStaff]

    def create(self, request, *args, **kwargs):
        """
        Create a new billing record.
        """
        bill_datas = request.data.get('items')
        customer_name = request.data.get('customer_name')
        if len(bill_datas) == 0:
            return Response({"detail": "No items in the bill."}, status=status.HTTP_400_BAD_REQUEST)
        total_amount = 0
        bill = Bill.objects.create(
            staff=request.user,
            customer_name=customer_name,
            total_amount=total_amount
        )
        bill_items = []
        valid_packing = dict(BillItem.PACKAGING_CHOICES).keys()
        for bill_data in bill_datas:
            medicine_id = bill_data.get('medicine')
            quantity = bill_data.get('quantity')
            packaging_type = bill_data.get('packaging_type')
            medicine = Medicine.objects.get(id=medicine_id)
            if medicine.stock_quantity < quantity:
                return Response({"detail": "Not enough stock for medicine."}, status=status.HTTP_400_BAD_REQUEST)
            if not medicine:
                return Response({"detail": "Medicine not found."}, status=status.HTTP_404_NOT_FOUND)
            if packaging_type not in valid_packing:
                return Response({"detail": "Invalid packaging type."}, status=status.HTTP_400_BAD_REQUEST)
            if packaging_type == 'single':
                unit_price = medicine.price_single
            elif packaging_type == 'strip' and medicine.price_strip is not None:
                unit_price = medicine.price_strip
            elif packaging_type == 'box' and medicine.price_box is not None:
                unit_price = medicine.price_box
            elif packaging_type == 'pack' and medicine.price_pack is not None:
                unit_price = medicine.price_pack
            bill_item = BillItem.objects.create(
                bill=bill,
                medicine=medicine,
                quantity=quantity,
                price=unit_price,
                subtotal=unit_price * quantity,
                packaging_type=packaging_type
            )
            total_amount += bill_item.subtotal
            bill_items.append(bill_item)
            medicine.stock_quantity -= quantity
            medicine.save()
        bill.total_amount = total_amount
        bill.save()
        serializer = BillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def perform_create(self, serializer):
        serializer.save(staff=self.request.user)