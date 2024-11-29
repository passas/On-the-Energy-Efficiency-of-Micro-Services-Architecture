from django.contrib.auth.models import User
from django.db import models

from decimal import Decimal

################################################# PRODUCT ##########################################################
class Product (models.Model):
    sku = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    materials = models.ManyToManyField("Material")
    sex = models.ForeignKey("Sex", on_delete=models.PROTECT)
    color = models.ForeignKey("Color", on_delete=models.PROTECT)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    price = models.ForeignKey("Price", on_delete=models.PROTECT, related_name="price_id", blank=True, null=True)
    description = models.TextField(max_length=512, blank=True, null=True)

    def price_today (self):

        price = self.price.price
        discount = self.price.discount

        today = float ( price )

        today = float(price) - ( float(price) * ( int(discount) / 100.0 ) )

        today = str (today )
        today = Decimal(today)

        return today
    
# Product Sex
class Sex (models.Model):
    SEX = [
        ("MAN", "Man"),
        ("WOMAN", "Woman"),
        ("OTHER", "Other"),
    ]
    sex = models.CharField(max_length=16, choices=SEX, unique=True)

    def __str__ (self):
        return f"{self.sex}"
    
    def save (self, *args, **kwargs):
        error = False

        # Sex
        _sex = {
            "MAN": "Man",
            "WOMAN": "Woman"
        }
        
        if self.sex.upper() in _sex:
            self.sex = _sex[self.sex.upper()]
        else:
            self.sex = "Other"
        
        # DB
        if error == False:
            super(Sex, self).save(*args, **kwargs)

# Product Category
class Category (models.Model):
    CATEGORY = [
        ("BLAZERS", "Blazers"),
        ("CARDIGANS", "Cardigans"),
        ("CASUAL SHIRTS", "Casual Shirts"),
        ("COATS", "Coats"),
        ("DRESSES", "Dresses"),
        ("FORMAL SHIRTS", "Formal Shirts"),
        ("HOODIES", "Hoodies"),
        ("HOODIES & SWEATSHIRTS", "Hoodies & Sweatshirts"),
        ("JACKETS", "Jackets"),
        ("JACKETS & COATS", "Jackets & Coats"),
        ("JEANS", "Jeans"),
        ("JOGGERS", "Joggers"),
        ("JUMPERS", "Jumpers"),
        ("JUMPSUITS", "Jumpsuits"),
        ("KNITWEAR", "Knitwear"),
        ("POLO SHIRTS", "Polo Shirts"),
        ("SHIRTS & BLOUSES", "Shirts & Blouses"),
        ("SHORTS", "Shorts"),
        ("SKIRTS", "Skirts"),
        ("SUITS", "Suits"),
        ("SWEATSHIRTS", "Sweatshirts"),
        ("T-SHIRTS", "T-Shirts"),
        ("T-SHIRTS & TOPS", "T-Shirts & Tops"),
        ("TROUSERS", "Trousers"),
        ("OTHER", "Other"),
    ]
    category = models.CharField(max_length=32, choices=CATEGORY, unique=True)

    def __str__ (self):
        return f"{self.category}"
    
    def save (self, *args, **kwargs):
        error = False

        # Category
        _category = {
            "BLAZERS": "Blazers",
            "CARDIGANS": "Cardigans",
            "CASUAL SHIRTS": "Casual Shirts",
            "COATS": "Coats",
            "DRESSES": "Dresses",
            "FORMAL SHIRTS": "Formal Shirts",
            "HOODIES": "Hoodies",
            "HOODIES & SWEATSHIRTS": "Hoodies & Sweatshirts",
            "JACKETS": "Jackets",
            "JACKETS & COATS": "Jackets & Coats",
            "JEANS": "Jeans",
            "JOGGERS": "Joggers",
            "JUMPERS": "Jumpers",
            "JUMPSUITS": "Jumpsuits",
            "KNITWEAR": "Knitwear",
            "POLO SHIRTS": "Polo Shirts",
            "SHIRTS & BLOUSES": "Shirts & Blouses",
            "SHORTS": "Shorts",
            "SKIRTS": "Skirts",
            "SUITS": "Suits",
            "SWEATSHIRTS": "Sweatshirts",
            "T-SHIRTS": "T-Shirts",
            "T-SHIRTS & TOPS": "T-Shirts & Tops",
            "TROUSERS": "Trousers",
        }

        if self.category.upper() in _category:
            self.category = _category[self.category.upper()]
        else:
            self.category = "Other"
        
        # DB
        if error == False:
            super(Category, self).save(*args, **kwargs)


# Product Material
class Material (models.Model):
    MATERIAL = [
        ("COTTON", "Cotton"),
        ("DENIM", "Denim"),
        ("WOOL", "Wool"),
        ("LEATHER", "Leather"),
        ("OTHER", "Other"),
    ]
    material = models.CharField(max_length=16, choices=MATERIAL)
    percentage = models.IntegerField()

    def __str__ (self):
        return f"{self.material} {self.percentage}"
    
    def save (self, *args, **kwargs):
        error = False

        # Material
        _material = {
            "COTTON": "Cotton",
            "DENIM": "Denim",
            "WOOL": "Wool",
            "LEATHER": "Leather",
            "OTHER": "Other",
        }

        if self.material.upper() in _material:
            self.material = _material[self.material.upper()]
        else:
            self.material = "Other"

        # Percentage
        percentage = int (self.percentage)
        if percentage < 1 and percentage > 100:
            error = True
        
        # DB
        if error == False:
            super(Material, self).save(*args, **kwargs)


# Product Color
class Color (models.Model):
    COLOR = [
        ("RED", "Red"),
	    ("DARK BLUE", "Dark Blue"),
	    ("BLUE", "Blue"),
	    ("GREEN", "Green"),
	    ("WHITE", "White"),
	    ("BLACK", "Black"),
	    ("BROWN", "Brown"),
	    ("ORANGE", "Orange"),
	    ("VIOLET", "Violet"),
	    ("PURPLE", "Purple"),
	    ("DARK RED", "Dark Red"),
	    ("DARK GREEN", "Dark Green"),
	    ("CAMEL", "Camel"),
	    ("YELLOW", "Yellow"),
	    ("OTHER", "Other"),
    ]
    color = models.CharField(max_length=16, choices=COLOR, unique=True)

    def __str__ (self):
        return f"{self.color}"
    
    def save (self, *args, **kwargs):
        error = False

        # Color
        _color = {
            "RED": "Red",
	        "DARK BLUE": "Dark Blue",
	        "BLUE": "Blue",
	        "GREEN": "Green",
	        "WHITE": "White",
	        "BLACK": "Black",
	        "BROWN": "Brown",
	        "ORANGE": "Orange",
	        "VIOLET": "Violet",
	        "PURPLE": "Purple",
	        "DARK RED": "Dark Red",
	        "DARK GREEN": "Dark Green",
	        "CAMEL": "Camel",
	        "YELLOW": "Yellow",
        }

        if self.color.upper() in _color:
            self.color = _color[self.color.upper()]
        else:
            self.color = "Other"
        
        # DB
        if error == False:
            super(Color, self).save(*args, **kwargs)


class Price (models.Model):
    product = models.ForeignKey("Product", on_delete=models.PROTECT, related_name="product_id")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def save (self, *args, **kwargs):
        error = False
        
        # Discount %
        discount = int ( self.discount )
        if discount < 1 and discount > 100:
            error = True
        
        # DB
        if error == False:
            super(Price, self).save(*args, **kwargs)


class Stock (models.Model):
    product = models.OneToOneField ("Product", on_delete=models.CASCADE)
    S = models.IntegerField()
    M = models.IntegerField()
    L = models.IntegerField()
    XL = models.IntegerField()

    def set_stock (self, size, stock):
        if size == "S":
            if (self.S + stock) >= 0:
                self.S = self.S + stock
            else:
                return False
        elif size == "M":
            if (self.M + stock) >= 0:
                self.M = self.M + stock
            else:
                return False
        elif size == "L":
            if (self.L + stock) >= 0:
                self.L = self.L + stock
            else:
                return False
        elif size == "XL":
            if (self.XL + stock) >= 0:
                self.XL = self.XL + stock
            else:
                return False
        
        self.save()
        return True
####################################################################################################################


################################################## CART ############################################################
class Cart (models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField ("CartProduct")
    updated = models.DateTimeField(auto_now=True)

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
    
    def delete (self):

        for product in self.products.all():
            product.delete()
        
        super(Cart, self).delete()

class CartProduct (models.Model):
    product = models.ForeignKey ("Product", on_delete=models.PROTECT)
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
    
    def count (self):

        return self.S + self.M + self.L + self.XL
    
    def save (self, *args, **kwargs):
        
        ground_zero = 0

        if self.S <= 0:
            ground_zero += 1
        
        if self.M <= 0:
            ground_zero += 1

        if self.L <= 0:
            ground_zero += 1

        if self.XL <= 0:
            ground_zero += 1
        
        # DB
        if ground_zero == 5:
            self.delete()
        else:
            super(CartProduct, self).save(*args, **kwargs)

    def total (self):

        total = 0.0
        
        if self.S > 0:
            total += float ( self.product.price_today() ) * self.S
        
        if self.M > 0:
            total += float ( self.product.price_today() ) * self.M
        
        if self.L > 0:
            total += float ( self.product.price_today() ) * self.L
        
        if self.XL > 0:
            total += float ( self.product.price_today() ) * self.XL

        return total
####################################################################################################################

################################################# PAYMENT ##########################################################
class Payment (models.Model):
    order = models.ForeignKey ("Order", on_delete=models.PROTECT, related_name="payed_date")
    method = models.ForeignKey ("PaymentMethod", on_delete=models.PROTECT, related_name="how")
    processes = models.DateTimeField (auto_now_add=True)

class PaymentMethod (models.Model):
    METHOD = [
        ("PAYPAL", "PayPal"),
        ("VISA", "Visa"),
        ("GIFT CARD", "Gift Card"),
        ("OTHER", "Other"),
    ]
    method = models.CharField(max_length=16, choices=METHOD, unique=True)

    def __str__ (self):
        return f"{self.method}"
    
    def save (self, *args, **kwargs):
        error = False

        # Method
        _method = {
            "PAYPAL": "PayPal",
            "VISA": "Visa",
            "GIFT CARD": "Gift Card",
        }

        if self.method.upper() in _method:
            self.method = _method[self.method.upper()]
        else:
            self.method = "Other"
        
        # DB
        if error == False:
            super(PaymentMethod, self).save(*args, **kwargs)
####################################################################################################################

################################################## BILL ############################################################
class Order (models.Model):
    user = models.ForeignKey (User, on_delete=models.PROTECT)
    products = models.ManyToManyField ("OrderProduct")
    ITIN = models.TextField (max_length=75, null=True, blank=True)

    def total (self):

        total = 0.0
        
        for product in self.products.all():
            total += product.total()

        return total

class OrderProduct (models.Model):
    product = models.ForeignKey ("Product", on_delete=models.PROTECT)
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

####################################################################################################################

################################################ SHIPPING ##########################################################
class Shipping (models.Model):
    order = models.ForeignKey ("Order", on_delete=models.PROTECT)
    method = models.ForeignKey ("ShippingMethod", on_delete=models.PROTECT)
    address = models.TextField (max_length=101)
    created = models.DateTimeField (auto_now_add=True)
    sented = models.DateTimeField (blank=True, null=True)

    def set_sented_to_now (self):
        from datetime import datetime
        self.sented = datetime.now()
        self.save()

class ShippingMethod (models.Model):
    METHOD = [
        ("DHL", "Dhl"),
        ("UPS", "Ups"),
        ("EXPRESS", "Correos Express"),
        ("STORE", "Store"),
        ("OTHER", "Other"),
    ]
    method = models.CharField(max_length=16, choices=METHOD, unique=True)

    def __str__ (self):
        return f"{self.method}"
    
    def save (self, *args, **kwargs):
        error = False

        # Method
        _method = {
            "DHL": "Dhl",
            "UPS": "Ups",
            "EXPRESS": "Correos Express",
            "STORE": "Store",
            "OTHER": "Other",
        }

        if self.method.upper() in _method:
            self.method = _method[self.method.upper()]
        else:
            self.method = _method["OTHER"]
        
        # DB
        if error == False:
            super(PaymentMethod, self).save(*args, **kwargs)
####################################################################################################################
