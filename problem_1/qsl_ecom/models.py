from django.db import models


class BaseTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseTimeModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Brand(BaseTimeModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Warranty(BaseTimeModel):
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.duration

class Seller(BaseTimeModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(BaseTimeModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
