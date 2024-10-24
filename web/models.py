from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    extra_info = models.JSONField()

    def __str__(self):
        return self.product_id