from .models import Cart, CartProduct


def get_cart ( user_id ):

    try:

        cartOrm = Cart.objects.get(user_id=user_id)

        products = set ()

        for product in cartOrm.products.all():

            products.add ( product.product_id )

    except Cart.DoesNotExist:
        
        cartOrm = None

        products = set ()

    return (cartOrm, products)



def add_to_cart (user_id, product_id, size):

    try:
        cartOrm = Cart.objects.get(user_id=user_id)
    except Cart.DoesNotExist:
        cartOrm = Cart.objects.create(user_id=user_id)
    
    try:
        cartProductOrm = cartOrm.products.get(product_id=product_id)
        cartProductOrm.set_stock(size, 1)
        cartProductOrm.save()

    except CartProduct.DoesNotExist:
        cartProductOrm = CartProduct.objects.create(product_id=product_id)
        cartProductOrm.set_stock(size, 1)
        cartProductOrm.save()

        cartOrm.products.add ( cartProductOrm )
        cartOrm.save()



def render_cart (product_table, cartOrm):

    cart = {
        "count": 0,
        "total": 0.0,
        "products": []
    }

    for product in cartOrm.products.all():

        id = product.product_id

        p = {}

        p["id"] = id
        p["name"] = product_table[id]["name"]
        p["color"] = product_table[id]["color"]
        p["stock"] = {
            "S": product.S,
            "M": product.M,
            "L": product.L,
            "XL": product.XL 
        } 
        p["price"] = {
            "price": product_table[id]["price"]["price"],
            "discount": product_table[id]["price"]["discount"]
        } 
        p["price_today"] = product_table[id]["price_today"]

        price = float ( p["price_today"] )
        total = product.total (price)
        p["total"] = total

        cart["products"].append ( p )
        
        cart["total"] += total

        cart["count"] += product.S + product.M + product.L + product.XL

    return cart



def cart_delete ( cartOrm ):

    cartOrm.delete()