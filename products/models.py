from django.db import models

# Create your models here.
class product_list(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics')

