from django.db import models
from apps.authentication.models import User
from apps.medicines.models import Medicine

class Bill(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'staff'})
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Bill #{self.id} by {self.staff.username}"

class BillItem(models.Model):
    PACKAGING_CHOICES = (
        ('single', 'Single'),
        ('strip', 'Strip'),
        ('pack', 'Pack'),
        ('box', 'Box'),
    )

    bill = models.ForeignKey(Bill, related_name='items', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    packaging_type = models.CharField(max_length=10, choices=PACKAGING_CHOICES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.medicine.name} - {self.quantity} {self.packaging_type}"