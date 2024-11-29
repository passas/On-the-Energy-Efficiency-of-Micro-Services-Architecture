from django.core.management.base import BaseCommand
from api.models import PaymentMethod

# python manage.py seed --mode=seed

""" Clear all data and creates addresses """
MODE_SEED = 'seed'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('Done.')


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

    :param mode: seed / auditoria_projeto 
    :return:
    """
    if mode == MODE_SEED:
        create_paymentMethod()