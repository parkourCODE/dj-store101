from django.db import models
from apps.items.models import Items
# Create your models here.
class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=111)
    totalPrice = models.FloatField()
    delivery_fee = models.IntegerField()


    def __str__(self):
        return self.id


class OrdersItems(models.Model):
    id_order_item = models.ForeignKey('Order.id_order', on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    addition = models.FloatField()
    discount = models.FloatField()