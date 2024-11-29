def send_order_invoice (email, first_name, last_name, payment_id, order_id, products): # Mock

    from django.core.mail import send_mail
    
    Message = ""

    Message += f"Hi {first_name},\n\n"

    Message += f"We're glad to inform you that your order as been processed.\n\n"

    Message += f"Product Name Color S M L XL Payed p/ product Discount Price\n\n\n"

    for product in products:

        name = product['name']
        color = product['color']
        S = product['stock']['S']
        M = product['stock']['M']
        L = product['stock']['L']
        XL = product['stock']['XL']
        payed = product['price_today']
        discount = product['price']['discount']
        price = product['price']['price']

        Message += f"{name}\t"

        Message += f"{color}\t"

        Message += f"{S}\t"

        Message += f"{M}\t"

        Message += f"{L}\t"

        Message += f"{XL}\t"

        Message += f"${payed}\t"

        Message += f"{discount}%\t"

        Message += f"${price}"

        Message += "\n\n"

    #send_mail(
    #    f"Boutique - Order#{order_id}",
    #    Message,
    #    "boutique@maildomain.com", # Put this in the credentials cfg file! Note to write an HTML mail template.
    #    [f"{email}"],
    #    fail_silently=False,
    #)

    return 200



def send_order_invoice_error (email, first_name, last_name, order_id, products): # Mock

    from django.core.mail import send_mail
    
    Message = ""

    Message += f"Hi {first_name},\n\n"

    Message += f"We're glad to inform you that your order as been processed.\n\n"

    Message += f"Product Name Color S M L XL Payed p/ product Discount Price\n\n\n"

    for product in products:

        name = product['name']
        color = product['color']
        S = product['stock']['S']
        M = product['stock']['M']
        L = product['stock']['L']
        XL = product['stock']['XL']
        payed = product['price_today']
        discount = product['price']['discount']
        price = product['price']['price']

        Message += f"{name}\t"

        Message += f"{color}\t"

        Message += f"{S}\t"

        Message += f"{M}\t"

        Message += f"{L}\t"

        Message += f"{XL}\t"

        Message += f"${payed}\t"

        Message += f"{discount}%\t"

        Message += f"${price}"

        Message += "\n\n"

    #send_mail(
    #    f"Boutique - Order#{order_id}",
    #    Message,
    #    "boutique@maildomain.com", # Put this in the credentials cfg file! Note to write an HTML mail template.
    #    [f"{email}"],
    #    fail_silently=False,
    #)

    return 200