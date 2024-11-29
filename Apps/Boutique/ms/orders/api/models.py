from django.db import models

from decimal import Decimal



class Order (models.Model):
    user_id = models.IntegerField ()
    products = models.ManyToManyField ("OrderProduct")
    ITIN = models.TextField (max_length=75, null=True, blank=True)

    def total (self):

        total = 0.0
        
        for product in self.products.all():
            total += product.total()

        return total
    
    def count (self):

        count = 0
        
        for product in self.products.all():
            count += product.count()

        return count

class OrderProduct (models.Model):
    product_id = models.IntegerField ()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.IntegerField(default=0)
    S = models.IntegerField(default=0)
    M = models.IntegerField(default=0)
    L = models.IntegerField(default=0)
    XL = models.IntegerField(default=0)

    def payed (self):

        price = self.price
        discount = self.discount

        ammount = float ( price )

        ammount = float(price) - ( float(price) * ( int(discount) / 100.0 ) )

        ammount = str (ammount )
        ammount = Decimal(ammount)

        return ammount
    
    def total (self):

        total = 0.0
        
        if self.S > 0:
            total += float ( self.payed() ) * self.S
        
        if self.M > 0:
            total += float ( self.payed() ) * self.M
        
        if self.L > 0:
            total += float ( self.payed() ) * self.L
        
        if self.XL > 0:
            total += float ( self.payed() ) * self.XL


        return total
    
    def count (self):

        return self.S + self.M + self.L + self.XL