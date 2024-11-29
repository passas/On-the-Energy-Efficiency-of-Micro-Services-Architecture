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