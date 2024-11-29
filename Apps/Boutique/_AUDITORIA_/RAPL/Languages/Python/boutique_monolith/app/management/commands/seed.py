from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Product, Sex, Category, Material, Color, Price, Stock
from app.models import PaymentMethod

# python manage.py seed --mode=auditoria_projeto

"""AA"""
MODE_AUDITORIA_USERS = 'auditoria_users'
"""AA"""
MODE_SEED = 'seed'
"""AA"""
MAX_DJANGO_INTEGER = 2147483647
"""AA"""
MODE_AUDITORIA_PROJETO = 'auditoria_products'




class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('Done.')
        # Feedback


def populate_users(first_name, last_name, email, password):
    
    instance = User (
                    first_name=first_name,
                    last_name=last_name,
                    username=email
                )
    
    instance.set_password(password)
    
    instance.save()

    print (instance)


def create_sex():
    SEX = [
        "Man",
        "Woman",
    ]
    for sex in SEX:
        Sex.objects.create(sex=sex)



def seed_category():
    CATEGORY = [
        "Blazers",
        "Cardigans",
        "Casual Shirts",
        "Coats",
        "Dresses",
        "Formal Shirts",
        "Hoodies",
        "Hoodies & Sweatshirts",
        "Jackets",
        "Jackets & Coats",
        "Jeans",
        "Joggers",
        "Jumpers",
        "Jumpsuits",
        "Knitwear",
        "Polo Shirts",
        "Shirts & Blouses",
        "Shorts",
        "Skirts",
        "Suits",
        "Sweatshirts",
        "T-Shirts",
        "T-Shirts & Tops",
        "Trousers",
    ]
    for category in CATEGORY:
        Category.objects.create(category=category)
        


def seed_color():
    COLOR = [
        "Red",
        "Dark Blue",
        "Blue",
        "Green",
        "White",
        "Black",
        "Brown",
        "Orange",
        "Violet",
        "Purple",
        "Dark Red",
        "Dark Green",
        "Camel",
        "Yellow",
        "Other",
    ]
    for color in COLOR:
        Color.objects.create(color=color)


def populate_products(id, sku, name, material, percentage, sex, color, category, price, discount, S=MAX_DJANGO_INTEGER, M=MAX_DJANGO_INTEGER, L=MAX_DJANGO_INTEGER, XL=MAX_DJANGO_INTEGER):
    
    materialOrm = Material.objects.create(material=material, percentage=percentage)
        
    sexOrm = Sex.objects.get(sex=sex)

    colorOrm = Color.objects.get(color=color)

    categoryOrm = Category.objects.get(category=category)

    productOrm = Product.objects.create(id=id,
                                        sku=sku,
                                        name=name,
                                        sex=sexOrm,
                                        color=colorOrm,
                                        category=categoryOrm)
    productOrm.materials.add( materialOrm )
        
    priceOrm = Price.objects.create(product=productOrm, price=price, discount=discount)

    productOrm.price = priceOrm
    productOrm.save()

    Stock.objects.create(product=productOrm, S=S, M=M, L=L, XL=XL)


def create_paymentMethod():
    METHOD = [
        "Other",
        "Visa",
        "PayPal",
        "Gift Card",
    ]
    for method in METHOD:
        PaymentMethod.objects.create(method=method)


    
def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: seed / auditoria_users 
    :return:
    """
    if mode == MODE_AUDITORIA_USERS:
        import csv

        with open('users.csv', mode ='r') as file:    
            csvFile = csv.DictReader(file)
            for line in csvFile:

                populate_users(
                    first_name = line["first_name"],
                    last_name = line["last_name"],
                    email = line["email"],
                    password = line["password"]
                )

    elif mode == MODE_SEED:
        create_sex()
        seed_category()
        seed_color()
        create_paymentMethod()

    elif mode == MODE_AUDITORIA_PROJETO:

        import csv

        with open('products.csv', mode ='r') as file:    
            csvFile = csv.DictReader(file)
            for line in csvFile:
                populate_products(
                    id = line["id"],
                    sku = line["sku"],
                    name = line["name"],
                    material = line["material"],
                    percentage = int ( line["percentage"] ),
                    sex = line["sex"],
                    color = line["color"],
                    category = line["category"],
                    price = line["price"],
                    discount = line["discount"],
                )