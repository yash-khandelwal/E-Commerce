from django.db import models

# Create your models here.
class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)