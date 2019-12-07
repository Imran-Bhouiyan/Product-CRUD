from django.conf import settings
from django.db import models
class Category(models.Model):
    category = models.CharField(max_length=1000)
    colours = models.CharField(max_length=1000,null=True)
    size = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.category_id)

class Product(models.Model):
    product_code = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100, null=False)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.TextField(max_length=100000,null=True)
    date = models.DateTimeField(null=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.product_code)