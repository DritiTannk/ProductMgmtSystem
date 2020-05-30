from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=60)
    manufacture_date = models.DateField()
    expiry_date =  models.DateField()
    product_mrp = models.DecimalField(max_digits=20, decimal_places=2)
    manufacture_name = models.CharField(max_length=100)

    def __str__(self):
        mystr = self.product_name + " " + self.manufacture_name + " " +str(self.product_mrp)
        return mystr

