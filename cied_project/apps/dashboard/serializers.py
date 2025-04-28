from rest_framework import serializers
from apps.medicines.models import Medicine


class MedicineStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'category', 'stock_quantity', 'expiry_date']