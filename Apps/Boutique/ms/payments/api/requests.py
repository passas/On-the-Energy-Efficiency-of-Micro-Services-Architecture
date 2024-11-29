import requests



def authenticate (jwt):

    headers = {
        'Authorization': f'Token {jwt}'
    }

    response = requests.get('http://127.0.0.1:8001/api/authenticate', headers=headers)

    if response.status_code == 200:

        data = response.json()

        if 'id' in data and 'email' in data and 'first_name' in data and 'last_name' in data: # Protocol

            return (200, data)
        
        else:

            return (500, {})
    
    elif response.status_code == 403:
    
        return (403, {})
    


def pay (total, payment): # Mock

    return (200, {})



def place_order (jwt, products, payment_options={}):

    data = {
        "JWT": jwt,
        "products": products,
        "ITIN": ""
    }

    r = requests.post(f'http://127.0.0.1:8005/api/register', json=data)
    
    status = r.status_code
    
    if status == 500:
        
        data = {}

    elif status == 200:

        data = r.json()

    return (status, data)



def send_order_invoice (jwt, payment, order_id, products):

    data = {
        "JWT": jwt,
        "payment": payment.id,
        "order": order_id,
        "products": products
    }

    r = requests.post('http://127.0.0.1:8006/api/invoice/order', json=data)

    status = r.status_code

    return (status, {})



def send_order_invoice_error (jwt, order_id, products):

    data = {
        "JWT": jwt,
        "order": order_id,
        "products": products
    }

    r = requests.post('http://127.0.0.1:8006/api/invoice/order', json=data)

    status = r.status_code

    return (status, {})