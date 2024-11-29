from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CartSerializer

from . import requests, utils



class cart (APIView):

    # login_required
    def get (self, request):
        
        # login_required
        if 'JWT' in request.data: # Protocol

            (status, user) = requests.authenticate ( request.data['JWT'] )

            if status == 403: # Expired session
            
                return Response (status=403, data={})
            
            (cart, products) = utils.get_cart ( user['id'] ) # User Id

            if cart is None: # Empty cart

                return Response (status=404, data={})
            
            (status, products) = requests.get_products ( products ) # Ids set

            if status == 404: # Products not found
                
                return Response(status=404, data={})
                
            elif status == 200: # Products dict
                
                cart = utils.render_cart (products, cart) # JSON

                return Response (status=200, data=cart)

        else: # Fail protocol

            return Response (status=403, data={})

    # login_required
    def post (self, request):
        
        # login_required
        if 'JWT' in request.data: # Protocol

            (status, user) = requests.authenticate ( request.data['JWT'] )

            if status == 403: # Expired session
            
                return Response (status=403, data={})
            
            if 'id' in request.data and 'size' in request.data: # Protocol
                
                (status, data) = requests.get_product (request.data['JWT'], request.data['id'], request.data['size'])

                if status == 403: # Expired session

                    return Response (status=403, data={})
                
                elif status == 404: # Product not found
                    
                    return Response (status=404, data={})

                elif status == 409: # Out of stock
                    
                    return Response (status=409, data={})

                elif status == 200: # Stocked
    
                    utils.add_to_cart (user['id'], request.data['id'], request.data['size'])

                    return Response (status=200, data={})
            
            else: # Failed protocol

                return Response (status=406, data={})
            


class purchase (APIView):

    # login_required
    def post (self, request):
        
        # login_required
        if 'JWT' in request.data: # Protocol

            (status, user) = requests.authenticate ( request.data['JWT'] )

            if status == 403: # Expired session
            
                return Response (status=403, data={})
            
            (cart, products) = utils.get_cart ( user['id'] ) # User Id

            if cart is None: # Empty cart

                return Response (status=404, data={})
            
            (status, products) = requests.get_products ( products ) # Ids set

            if status == 404: # Products not found
                
                return Response(status=404, data={})
                
            elif status == 200: # Products dict
                
                cartOrm = cart

                cart = utils.render_cart (products, cart) # JSON
            
                (status, _ ) = requests.pay ( request.data['JWT'], cart["total"], cart["products"], {})
                
                if status != 200:

                    return Response (status=400, data={})

                elif status == 200: 

                    utils.cart_delete ( cartOrm )

                    return Response (status=200, data={})