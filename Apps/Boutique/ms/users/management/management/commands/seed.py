from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# python manage.py seed --mode=auditoria_projeto

""" Clear all data and do not create any object """
MODE_AUDITORIA_PROJETO = 'auditoria_projeto'



class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('Done.')



def populate_users(first_name, last_name, email, password):
    
    instance = User (
                    first_name=first_name,
                    last_name=last_name,
                    username=email
                )
    
    instance.set_password(password)
    
    instance.save()

    print (instance)
    
    
def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: seed / auditoria_projeto 
    :return:
    """

    if mode == MODE_AUDITORIA_PROJETO:

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
