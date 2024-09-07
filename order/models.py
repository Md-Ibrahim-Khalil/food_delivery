from django.db import models
from restaurant.models import Restaurant
from django.conf import settings 
from django.contrib.auth.models import User


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, choices=[('card', 'Card'), ('cash', 'Cash')])
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"