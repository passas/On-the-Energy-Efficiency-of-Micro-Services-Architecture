from rest_framework.views import APIView
from rest_framework.response import Response

from . import requests, utils



class register (APIView):
    
    # login required
    def post (self, request):

        # login_required
        if 'JWT' in request.data: # Protocol

            (status, user) = requests.authenticate ( request.data['JWT'] )

            if status == 403: # Expired session
            
                return Response (status=403, data={})
        
        if 'products' in request.data and 'ITIN' in request.data: # Protocol

            order = utils.register (user['id'], request.data['products'], request.data['ITIN'])

            if order is None: # Error

                return Response (status=500, data={})
            
            data = {
                "id": order.id
            }

            return Response (status=200, data=data)

        else: # Wrong protocol

            return Response (status=406, data={})
