from .models import Order, OrderProduct



def register (user_id, products, itin):

    try:
        
        orderOrm = Order.objects.create(user_id=user_id)

        for product in products:

            productOrm = OrderProduct.objects.create (
                product_id=product['id'],
                price=product['price']['price'],
                discount=product['price']['discount'],
                S=product['stock']['S'],
                M=product['stock']['M'],
                L=product['stock']['L'],
                XL=product['stock']['XL']
            )

            orderOrm.products.add ( productOrm )
            orderOrm.save()

    except Order.DoesNotExist:
        
        orderOrm = None

    return orderOrm
    
    