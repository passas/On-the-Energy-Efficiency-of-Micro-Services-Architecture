from django.db import models

from decimal import Decimal


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