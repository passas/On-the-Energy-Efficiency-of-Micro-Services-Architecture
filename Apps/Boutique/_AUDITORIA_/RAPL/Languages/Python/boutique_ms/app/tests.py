from django.test.utils import setup_test_environment

from django.test import TestCase, Client


class AuditoriaTestCase(TestCase):


    def setUp(self):
        '''
        State an HTTP client.
        '''
        self.client = Client()


    def test_categories(self):
        '''
        Test if categories were well seed.
        '''
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["man_categories"]), 16)
        self.assertEqual(len(response.context["woman_categories"]), 12)


    def test_man (self):
        '''
        Test if man products were, at least, total seeded.
        '''
        response = self.client.get("/man")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["products"]), 1776)


    def test_woman (self):
        '''
        Test if man products were, at least, total seeded.
        '''
        response = self.client.get("/woman")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["products"]), 1714)


    def test_login (self):
        response = self.client.post("/login", {"email": "Jillayne.Cookie.1@yopmail.com", "password": "QUzzNVkU"})
        self.assertEqual(response.status_code, 200)


    def test_auditoria_1 (self):
        
        USERS = 1
        CATEGORIAS = 1
        PRODUTOS = 600

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


                    response = self.client.get (f"/man/{categoria}")
                    self.assertEqual(response.status_code, 200)
                    
                    products_all = response.context['products']
                    products_len = len ( products_all )

                    # Consultar produto
                    for k in range (0, PRODUTOS):
                        prod_i = k % products_len
                        produto = products_all[prod_i]['id']
                        response = self.client.get (f"/{produto}")
                        self.assertEqual(response.status_code, 200)

                        # Encomendar produto
                        response = self.client.post("/cart", {"id": produto, "size": "M"})
                        self.assertEqual(response.status_code, 302)

                # Visitar carrinho
                response = self.client.get("/cart")
                self.assertEqual(response.status_code, 200)
                total = CATEGORIAS * PRODUTOS
                self.assertEqual( response.context["count"], total )

                # Pagar carrinho
                response = self.client.post("/cart/purchase")
                self.assertEqual(response.status_code, 200)
                self.assertTrue ( "Thank you for purchasing with us." in response.context['messages'] )

                # Visitar carrinho
                response = self.client.get("/cart")
                self.assertEqual(response.status_code, 200)
                self.assertEqual( len(response.context["products"]), 0 )

