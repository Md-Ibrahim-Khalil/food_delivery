from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
                    "id",
                    "restaurant",
                    "total_amount",
                    "is_paid",
                    "payment_method",
                    "status",
                 ]