from django.db import models
from django.contrib.auth.models import User

class MenuItem(models. Model):
    name = models.CharField(max_length=100)
    description= models.TextField()
    price= models.DecimalField(max_digits=8, decimal_places=2)


    def_str_(self):
        return self.name

        class Order(models.Model)
        STATUS_CHOICES=[
            ('PENDING', 'Pending'),
            ('CONFIRMED', 'Confirmed'),
            ('PREPARING', 'Preparing'),
            ('CANCELLED', 'Cancelled'),
        ]

        customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
        order_items= models.ManyToManyField(MenuItem, through="OrderItem")
        total_amount= models.DecimalField(max_digits=8, decimal_places=2)
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
        created_at= models.DateTimeFields(auto_now_add=True)

        def_str_(self):
            return f"Order #{self.id} by {self.customer.username}"

            class OrderItem(models.Model)
            order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items_details")
            menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
            quantity = models.PositiveIntegerField,(default=1)

            def_str_(self):
                return f"{self.quantity} x {self.menu_item.name} (order #{self.order.id})"

 