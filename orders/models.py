from django.db import models


from django.contrib .auth.models import user
from products.models import MenuItem

class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','pending'),
        ('COMPLETED','Completed'),
        ('CANCELLED','Cancelled'),
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(MenuItem)
    total_amount=models.DecimalField(max_digits=8,decimal_palces=2)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"Order #{self.id}-{self.customer.username}"