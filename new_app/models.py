from django.db import models

class trip(models.Model):
    #id:int
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    descrption = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
# Create your models here.
