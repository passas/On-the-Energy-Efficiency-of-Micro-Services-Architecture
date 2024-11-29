from django.db import models



class Cart (models.Model):
    user_id = models.IntegerField (unique=True)
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField ("CartProduct")
    updated = models.DateTimeField(auto_now=True)
    
    def delete (self):

        for product in self.products.all():
            product.delete()
        
        super(Cart, self).delete()

class CartProduct (models.Model):
    product_id = models.IntegerField ()
    S = models.IntegerField(default=0)
    M = models.IntegerField(default=0)
    L = models.IntegerField(default=0)
    XL = models.IntegerField(default=0)

    def set_stock (self, size, stock):
        if size == "S":
            self.S = self.S + stock
        elif size == "M":
            self.M = self.M + stock
        elif size == "L":
            self.L = self.L + stock
        elif size == "XL":
            self.XL = self.XL + stock

        if self.S <= 0 and self.M <=0 and self.L <= 0 and self.XL <=0:
            self.delete()

    def total (self, price):
        
        total = 0.0

        if self.S > 0:
            total += self.S * price
        if self.M > 0:
            total += self.M * price
        if self.L > 0:
            total += self.L * price
        if self.XL > 0:
            total += self.XL * price

        return total
    
    