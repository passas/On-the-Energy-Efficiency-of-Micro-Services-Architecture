from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductSerializer

from . import utils, requests



class man_categories (APIView):
    
    def get (self, request):
        
        categories = utils.man_categories ()

        return Response (data=categories, status=200)
    


class woman_categories (APIView):
    
    def get (self, request):
        
        categories = utils.woman_categories ()

        return Response (data=categories, status=200)
    


class man (APIView):

    def get (self, request):
        
        products = utils.all_man ()

        serializer = ProductSerializer(products, many=True)
            
        data = serializer.data
        
        return Response (data=data, status=200)
    


class woman (APIView):

    def get (self, request):
        
        products = utils.all_woman ()

        serializer = ProductSerializer(products, many=True)
            
        data = serializer.data
        
        return Response (data=data, status=200)
    


class man_category (APIView):
    
    def get (self, request, category):
        
        (error, products) = utils.man_category( category )

        if error == "None":
        
            serializer = ProductSerializer(products, many=True)
            
            data = serializer.data
        
            return Response (data=data, status=200)

        elif error == "Category":

            data = {
                "detail": "Category not found."
            }

            return Response (data=data, status=404)


class woman_category (APIView):
    
    def get (self, request, category):
        
        (error, products) = utils.woman_category( category )

        if error == "None":
        
            serializer = ProductSerializer(products, many=True)
            
            data = serializer.data
        
            return Response (data=data, status=200)

        elif error == "Category":

            data = {
                "detail": "Category not found."
            }

            return Response (data=data, status=404)
        


class id (APIView):
    
    def get (self, request, id):
        
        product = utils.product ( id )

        if product is None:

            status = 404

            data = {}

        else:

            status = 200

            serializer = ProductSerializer(product, many=False)
            
            data = serializer.data
        
        return Response (data=data, status=status)
    


class get_product (APIView):

    # login required
    def get (self, request, id, size):

        # login_required
        if "JWT" in request.data: # Protocol

            (status, data) = requests.authenticate ( request.data["JWT"] )

            if status == 403: # Expired session
            
                return Response (status=403, data={})
            
            (product, stock) = utils.get_product (id, size)

            if product is None: # Prodcut not found

                return Response (status=404, data={})
            
            elif stock == False: # Stock unavailable

                return Response (status=409, data={})
            
            else: # Stocked

                return Response (status=200, data={})
            


class bulk (APIView):
    
    def get (self, request):

        if 'ids' in request.data: # Protocol

            products = utils.get_products( request.data['ids'] )

            if products is None: # No products found

                return Response (status=404, data={})

            serializer = ProductSerializer (products, many=True)

            data = serializer.data

            return Response (status=200, data=data)
        
        else: # Fail protocol

            return Response (status=406, data={})