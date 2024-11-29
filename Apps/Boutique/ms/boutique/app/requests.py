import requests



def all_man_categories():

    r = requests.get('http://127.0.0.1:8002/api/man/categories')
    
    categories = r.json()

    return categories
    
    

def all_woman_categories():

    r = requests.get('http://127.0.0.1:8002/api/woman/categories')

    categories = r.json()

    return categories



def all_man():

    r = requests.get('http://127.0.0.1:8002/api/man')

    products = r.json()

    return products




def all_woman():

    r = requests.get('http://127.0.0.1:8002/api/woman')

    products = r.json()

    return products



def man_category ( category ):

    r = requests.get(f'http://127.0.0.1:8002/api/man/{category}')
    
    if r.status_code == 200:
        
        products = r.json()

    elif r.status_code == 404:

        products = []

    return (r.status_code, products)



def woman_category ( category ):

    r = requests.get(f'http://127.0.0.1:8002/api/woman/{category}')
    
    if r.status_code == 200:
        
        products = r.json()

    elif r.status_code == 404:

        products = []

    return (r.status_code, products)



def product ( id ):

    r = requests.get(f'http://127.0.0.1:8002/api/{id}')

    if r.status_code == 200:
        
        product = r.json()

        status = 200

    else:

        product = {}

        status = 404

    return (r.status_code, product)




def get_cart ( jwt ):

    data = {
        "JWT": jwt
    }

    r = requests.get(f'http://127.0.0.1:8003/api/cart', data=data)
    
    if r.status_code == 200:
        
        data = r.json()

        if 'total' in data and 'products' in data: # Protocol
    
            return (200, r.json())
        
        else:
            
            return (206, {})
    
    elif r.status_code == 403:

        return (403,{})
    
    else:

        return (404,{})
    


def post_cart (jwt, product_id, size):

    data = {
        "JWT": jwt,
        "id": product_id,
        "size": size
    }

    r = requests.post(f'http://127.0.0.1:8003/api/cart', data=data)
    
    status = r.status_code
    
    if status == 403:
        
        data = {}

    elif status == 404:

        data = {}

    elif status == 409:

        data = {}

    return (status, data)
    


def purchase_cart (jwt):

    data = {
        "JWT": jwt
    }

    r = requests.post(f'http://127.0.0.1:8003/api/cart/purchase', data=data)

    status = r.status_code

    if status == 400:

        data = {}

    elif status == 200:

        data = {}

    return (status, data)
    


def login (email, password):

    data = {
        "username": email,
        "password": password
    }

    r = requests.post('http://127.0.0.1:8001/api/login', data=data)

    if r.status_code == 200:

        data = r.json()

        if 'user_id' in data and 'token' in data: # Protocol

            return (200, data)

    elif r.status_code == 404:

        data = {
            "detail": "Email and/or password incorrect."
        }

        return (404, data)

    elif r.status_code == 403:

        data = {
            "detail": "Forbidden."
        }

        return (403, data)
    


def register (email, password, first_name, last_name):

    data = {
        "username": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
    }

    r = requests.post('http://127.0.0.1:8001/api/register', data=data)

    if r.status_code == 200:

        data = r.json()

        if 'user_id' in data and 'token' in data: # Protocol

            return (200, data)

    elif r.status_code == 400:

        data = {
            "detail": "Email already in use."
        }

        return (400, data)
    


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