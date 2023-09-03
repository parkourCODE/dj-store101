from django.db import models
from apps.orders.models import Order
# Create your models here.
class SubItems(models.Model):
    id_sub_items = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()

class Items(models.Model):
    id_items = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class OrdersItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    sub_items_id = models.ForeignKey(SubItems, on_delete=models.CASCADE)
    parent_item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    addition = models.FloatField()
    discount = models.FloatField()




