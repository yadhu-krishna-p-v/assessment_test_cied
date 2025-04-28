from rest_framework import serializers
from apps.medicines.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'category', 'price_single', 'price_strip', 'price_pack', 'price_box', 'stock_quantity', 'expiry_date']