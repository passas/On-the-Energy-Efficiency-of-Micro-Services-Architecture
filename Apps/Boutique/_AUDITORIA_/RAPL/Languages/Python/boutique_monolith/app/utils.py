from .models import Product, Category, Sex
from .models import Stock
from .models import Cart, CartProduct
from .models import Order, OrderProduct
from .models import Payment, PaymentMethod


def all_man_categories ():
    #all = Category.objects.all().values_list('category', flat=True)

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



def all_woman_categories ():

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

    all = Product.objects.filter(sex=sexOrm).all().order_by("category", "id", "name")

    return all



def all_woman ():
    
    SEX = "Woman"

    sexOrm = Sex.objects.get(sex=SEX)

    all = Product.objects.filter(sex=sexOrm).all().order_by("category", "id", "name")

    return all


def all_man_category (category):

    SEX = "Man"

    sexOrm = Sex.objects.get(sex=SEX)

    categoryOrm = Category.objects.get(category=category)

    all = Product.objects.filter(sex=sexOrm, category=categoryOrm).all().order_by("id", "name")

    return all


def all_woman_category (category):

    SEX = "Woman"

    sexOrm = Sex.objects.get(sex=SEX)

    categoryOrm = Category.objects.get(category=category)

    all = Product.objects.filter(sex=sexOrm, category=categoryOrm).all().order_by("id", "name")

    return all

def product_id ( id ):
    
    try:
        productOrm = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        productOrm = None

    return productOrm

def get_from_stock (product_id, size):

    stockOrm_success = True
    stock_success = False

    try:
        stockOrm = Stock.objects.get(product_id=product_id)

        stock_success = stockOrm.set_stock (size, -1)

    except Stock.DoesNotExist:
        
        stockOrm_success = False

    return {
        "product_id": stockOrm_success,
        "size": stock_success
    }


def add_to_cart (user, product_id, size):

    try:
        cartOrm = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cartOrm = Cart.objects.create(user=user)

    try:
        productOrm = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return False

    try:
        cartProductOrm = cartOrm.products.get(product=productOrm)
        cartProductOrm.set_stock(size, 1)
        cartProductOrm.save()

    except CartProduct.DoesNotExist:
        cartProductOrm = CartProduct.objects.create(product=productOrm)
        cartProductOrm.set_stock(size, 1)
        cartProductOrm.save()

        cartOrm.products.add ( cartProductOrm )



def my_cart ( user ):

    try:
        cartOrm = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cartOrm = None

    return cartOrm


def payAPI (user, ammount): # Mock

    return True


def create_order ( userOrm, cartOrm ):

    orderOrm = Order.objects.create(user=userOrm)

    for cart_product in cartOrm.products.all():

        p = OrderProduct.objects.create (
                product=cart_product.product,
                price=cart_product.product.price.price,
                discount=cart_product.product.price.discount,
                S=cart_product.S,
                M=cart_product.M,
                L=cart_product.L,
                XL=cart_product.XL
            )
        orderOrm.products.add ( p )
        orderOrm.save()

    return orderOrm


def create_payment ( orderOrm ):
    
    try: # Mock
        
        paymentMethodOrm = PaymentMethod.objects.get( method = "Paypal" )

    except PaymentMethod.DoesNotExist:
        
        paymentMethodOrm = PaymentMethod.objects.get( pk=1 )

    Payment.objects.create ( order=orderOrm, method=paymentMethodOrm )


def send_order_invoice ( orderOrm, user ):

    from django.core.mail import send_mail
    
    Message = ""

    Message += f"Hi, {user.first_name},\n\n"

    Message += f"We're glad to inform you that your order as been processed.\n\n"

    Message += f"Product Name Color S M L XL Payed p/ product Discount Price\n\n\n"

    for prod in orderOrm.products.all():

        Message += f"{prod.product.name}\t"

        Message += f"{prod.product.color}\t"

        Message += f"{prod.S}\t"

        Message += f"{prod.M}\t"

        Message += f"{prod.L}\t"

        Message += f"{prod.XL}\t"

        Message += f"${prod.total}\t"

        Message += f"{prod.discount}%\t"

        Message += f"${prod.price}"

    #send_mail(
    #    f"Boutique - Order#{orderOrm.id}",
    #    Message,
    #    "boutique@maildomain.com", # Put this in the credentials cfg file! Note to write an HTML mail template.
    #    [f"{user.email}"],
    #    fail_silently=False,
    #)

def my_orders ( userOrm ):

    orders = Order.objects.filter ( user=userOrm ).all()

    return orders