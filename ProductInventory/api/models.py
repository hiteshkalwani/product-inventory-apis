from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def status_enum(self):
        return 'available' if self.status else 'unavailable'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically set status to False if quantity is 0
        if self.quantity == 0:
            self.status = False
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
