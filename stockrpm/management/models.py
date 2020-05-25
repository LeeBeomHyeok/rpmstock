from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=20)
    num = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Owner(models.Model):
    
    name = models.CharField(max_length=20, default='cargo')
    num = models.IntegerField(default=0)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name