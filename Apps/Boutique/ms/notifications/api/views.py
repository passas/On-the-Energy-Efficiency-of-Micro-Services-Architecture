from rest_framework.views import APIView
from rest_framework.response import Response

from . import utils, requests



class order_invoice (APIView):

    # login required
    def post (self, request):

        # login_required
        if 'JWT' in request.data: # Protocol

            (status, user) = requests.authenticate ( request.data['JWT'] )

            if status == 403: # Expired session
            
                return Response (status=403, data={})
        
        if 'payment' in request.data and 'order' in request.data and 'products' in request.data: # Protocol

            status = utils.send_order_invoice (user['email'], user['first_name'], user['last_name'], request.data['payment'], request.data['order'], request.data['products']) # Mock

            return Response (status=200, data={})
        
        elif 'order' in request.data and 'products' in request.data: # Protocol

            status = utils.send_order_invoice_error (user['email'], user['first_name'], user['last_name'], request.data['order'], request.data['products']) # Mock

            return Response (status=200, data={})
        
        else: # Wrong protocol

            return Response (status=406, data={})