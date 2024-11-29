from rest_framework.views import APIView
from rest_framework.response import Response

from . import requests, utils



class pay (APIView):
    
    # login required
    def post (self, request):

        # login_required
        if 'JWT' in request.data: # Protocol

            (status, user) = requests.authenticate ( request.data['JWT'] )

            if status == 403: # Expired session
            
                return Response (status=403, data={})
        
        if 'total' in request.data and 'products' in request.data and 'payment' in request.data: # Protocol

            (status, info) = requests.pay ( request.data['total'], request.data['payment'] ) #3rd Party-API

            if status == 403: # Non autherized

                return Response (status=403, data={})
            
            elif status == 404: # Wrong credentials

                return Response (status=404, data={})
            
            elif status == 200:
                
                (status, order) = requests.place_order ( request.data['JWT'], request.data['products'] )

                if status == 500: # Error

                    return Response (status=500, data={})

                elif status == 200:

                    payment = utils.create_payment (order['id'], info, request.data['total'])

                    if payment is None: # Error

                        (status, data) = requests.send_order_invoice_error (request.data['JWT'], order['id'], request.data['products'])

                        return Response (status=200, data={})
                    
                    else:
                        
                        (status, data) = requests.send_order_invoice (request.data['JWT'], payment, order['id'], request.data['products'])

                        return Response (status=200, data={})

        else: # Failed protocol

            return Response (status=406, data={})