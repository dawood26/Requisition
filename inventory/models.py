from django.db import models
from department.models import *
from vendor.models import *

# Create your models here.
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.CharField(max_length=30)
    unitprice= models.FloatField()
    totalprice= models.FloatField()
    instructution = models.CharField(max_length=30)
    requisitioner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created= models.DateTimeField(default=datetime.datetime.now())
    message=''
    