from django.core.management.base import BaseCommand
import unittest
from django.test.utils import setup_test_environment

class Command(BaseCommand):
    help = """
    If you need Arguments, please check other modules in 
    django/core/management/commands.
    """

    def handle(self, **options):
        setup_test_environment()
        suite = unittest.TestLoader().loadTestsFromTestCase(AuditoriaTestCase)
        unittest.TextTestRunner().run(suite)


from django.test import TestCase, Client
from app.models import Product, Cart

class AuditoriaTestCase(TestCase):

    def setUp(self):
        '''
        State an HTTP client.
        '''
        self.client = Client()

        
    def test_auditoria_1 (self):
        
        USERS = 1
        CATEGORIAS = 1
        PRODUTOS = 128

        import csv

        with open('users.csv', mode ='r') as file:    
            
            UTILIZADORES = list ( csv.DictReader(file) )
            
            N = len (UTILIZADORES)

            STEP = int( N / USERS ) + 1

            # Utilizadores
            for i in range (0, N, STEP):

                utilizador = UTILIZADORES[i]
                
                email = utilizador["email"]
                password = utilizador["password"]

                # Login
                response = self.client.post("/login", {"email": email, "password": password})
                self.assertEqual(response.status_code, 302)
                
                # Visitar categoria
                CAT = ["Blazers", "Cardigans", "Casual Shirts", "Coats", "Formal Shirts", "Hoodies", "Jackets", "Jeans", "Joggers", "Jumpers", "Polo Shirts", "Shorts", "Suits", "Sweatshirts", "T-Shirts", "Trousers"]
                CAT_I = 0
                CAT_LEN = len (CAT)
                for j in range (0, CATEGORIAS):
                    categoria = CAT[CAT_I]
                    CAT_I = (CAT_I + 1) % CAT_LEN
#
                    response = self.client.get (f"/products/man/{categoria}")
                    self.assertEqual(response.status_code, 200)
                    
                    product_all = response.context['products']
                    prod_total = len( product_all )

                    # Consultar produto
                    for k in range (0, PRODUTOS):
                        prod_i = k % prod_total 
                        prod_id = product_all[prod_i].id
                        response = self.client.get (f"/products/{prod_id}")
                        self.assertEqual(response.status_code, 200)
#
                        # Encomendar produto
                        SIZE = "M"
                        response = self.client.post("/add-to-cart", {"product_id": prod_id, "size": SIZE})
                        self.assertEqual(response.status_code, 302)

                # Visitar carrinho
                response = self.client.get("/cart")
                self.assertEqual(response.status_code, 200)
                cart = response.context['cart']
                total_cart_products = cart.count()
                total_watited = CATEGORIAS * PRODUTOS
                self.assertEqual( total_cart_products, total_watited )

                # Pagar carrinho
                response = self.client.post("/cart/purchase")
                self.assertEqual(response.status_code, 200)
                self.assertTrue ( "Thank you for purchasing with us." in response.context['messages'] )

                # Visitar carrinho
                response = self.client.get("/cart")
                self.assertEqual(response.status_code, 200)
                self.assertFalse( 'cart' in response.context )