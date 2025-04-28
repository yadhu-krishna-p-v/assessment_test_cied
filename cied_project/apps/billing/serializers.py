from rest_framework import serializers
from apps.medicines.models import Medicine
from apps.authentication.models import User
from apps.billing.models import Bill, BillItem
from apps.medicines.serializers import MedicineSerializer


class BillItemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)

    class Meta:
        model = BillItem
        fields = ['id', 'medicine', 'quantity', 'price_per_item', 'total_price']
        

class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Bill
        fields = ['id', 'user', 'total_amount', 'items', 'created_at']
