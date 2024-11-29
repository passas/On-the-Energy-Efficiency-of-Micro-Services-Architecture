from .models import Payment, PaymentMethod



def create_payment (order_id, info, total):

    try:
        
        paymentMethodOrm = PaymentMethod.objects.get(method="Visa")

    except PaymentMethod.DoesNotExist:

        paymentMethodOrm = PaymentMethod.objects.get(pk=1) # Unknown

    try:

        paymentOrm = Payment.objects.create(order_id=order_id, method = paymentMethodOrm)

    except Payment.DoesNotExist:
        
        paymentOrm = None

    return paymentOrm