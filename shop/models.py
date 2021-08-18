from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    wallet = models.IntegerField(default=10000)

class Item(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    in_stock = models.IntegerField(null=False, blank=False)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='purchases')
    item = models.ForeignKey(Item, on_delete=CASCADE, related_name='purchases')
    amount = models.IntegerField(null=False, blank=False)
    bought_at = models.DateTimeField(auto_now=True)

class Return(models.Model):
    purchase = models.OneToOneField(Purchase, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now=True)


