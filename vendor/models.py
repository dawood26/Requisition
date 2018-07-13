from django.db import models
import datetime
# Create your models here.
class Vendor(models.Model):
    vn_name = models.CharField(max_length=30)
    vn_phone = models.CharField(max_length=30)
    vn_email = models.CharField(max_length=30)
    vn_address = models.CharField(max_length=30)
    vn_created= models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):

        return self.vn_name

class Product(models.Model):
    p_name = models.CharField(max_length=30)
    p_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    p_created= models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.p_name
    
    def getAll(self):
        
        return Product.objects.all()
    
    
        
    
     
   
