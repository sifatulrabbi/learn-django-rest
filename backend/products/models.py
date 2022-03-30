from xml.etree.ElementInclude import default_loader
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
