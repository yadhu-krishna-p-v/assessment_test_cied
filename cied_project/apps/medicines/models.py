from django.db import models

class Medicine(models.Model):
    CATEGORY_CHOICES = (
        ('tablet', 'Tablet'),
        ('capsule', 'Capsule'),
        ('syrup', 'Syrup'),
        ('injection', 'Injection'),
        ('ointment', 'Ointment'),
        ('cream', 'Cream'),
        ('drop', 'Drop'),
        ('inhaler', 'Inhaler'),
    )

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price_single = models.DecimalField(max_digits=10, decimal_places=2)
    price_strip = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_pack = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_box = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name