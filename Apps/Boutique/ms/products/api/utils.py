from .models import Product, Sex, Category
from .models import Stock


def man_categories ():

    categories = [
        "Blazers",
        "Cardigans",
        "Casual Shirts",
        "Coats",
        "Formal Shirts",
        "Hoodies",
        "Jackets",
        "Jeans",
        "Joggers",
        "Jumpers",
        "Polo Shirts",
        "Shorts",
        "Suits",
        "Sweatshirts",
        "T-Shirts",
        "Trousers",
    ]
    
    categories.sort()

    return categories



def woman_categories ():

    categories = [
        "Blazers",
        "Coats",
        "Dresses",
        "Hoodies & Sweatshirts",
        "Jackets & Coats",
        "Jumpsuits",
        "Knitwear",
        "Polo Shirts",
        "Shirts & Blouses",
        "Skirts",
        "T-Shirts & Tops",
        "Trousers",
    ]
    
    categories.sort()

    return categories



def all_man ():

    SEX = "Man"

    sexOrm = Sex.objects.get(sex=SEX)

    products = Product.objects.filter(sex=sexOrm).all().order_by("category", "id", "name")

    return products



def all_woman ():

    SEX = "Woman"

    sexOrm = Sex.objects.get(sex=SEX)

    products = Product.objects.filter(sex=sexOrm).all().order_by("category", "id", "name")

    return products



def man_category ( category ):

    SEX = "Man"

    sexOrm = Sex.objects.get(sex=SEX)
    
    try:

        categoryOrm = Category.objects.get(category=category)

    except Category.DoesNotExist:

        return ("Category", [])

    products = Product.objects.filter(sex=sexOrm, category=categoryOrm).all().order_by("id", "name")

    return ("None", products)



def woman_category ( category ):

    SEX = "Woman"

    sexOrm = Sex.objects.get(sex=SEX)

    try:

        categoryOrm = Category.objects.get(category=category)

    except Category.DoesNotExist:

        return ("Category", [])

    products = Product.objects.filter(sex=sexOrm, category=categoryOrm).all().order_by("id", "name")

    return ("None", products)



def product ( id ):

    try:

        productOrm = Product.objects.get(pk=id)

    except Product.DoesNotExist:
        
        productOrm = None

    return productOrm



def get_product (product_id, size):

    stock = False

    try:
        stockOrm = Stock.objects.get(product_id=product_id)

        stock = stockOrm.set_stock (size, -1)

    except Stock.DoesNotExist:
        
        stockOrm = None

    return (stockOrm, stock)



def get_products ( ids ):

    try:

        products = Product.objects.filter(pk__in=ids).all()

    except Product.DoesNotExist:
        
        products = None

    return products