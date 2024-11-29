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
    


def get_product (jwt, id, size):

    data = {
        "JWT": jwt
    }

    r = requests.get(f'http://127.0.0.1:8002/api/{id}/{size}', data=data)

    status = r.status_code
    
    if status == 403:
        
        data = {}

    elif status == 404:

        data = {}

    elif status == 409:

        data = {}

    return (status, data)



def get_products (ids):

    # Serialize
    ids_json = []
    for id in ids:
        ids_json.append ( id )

    data = {
        "ids": ids_json
    }

    r = requests.get(f'http://127.0.0.1:8002/api/bulk', json=data)

    status = r.status_code
    
    if status == 404:
        
        data = {}

    elif status == 406:

        data = {}

    elif status == 200:

        data = r.json()

        # Dictionary
        products = {}

        for item in data:
            
            products[item["id"]] = item

        data = products
        
    return (status, data)



def pay (jwt, total, products, payment_options={}):

    data = {
        "JWT": jwt,
        "total": total,
        "products": products,
        "payment": payment_options
    }

    r = requests.post(f'http://127.0.0.1:8004/api/pay', json=data)
    
    status = r.status_code
    
    if status == 403:
        
        data = {}

    elif status == 404:

        data = {}

    elif status == 409:

        data = {}

    elif status == 200:

        data = {}

    return (status, data)
    