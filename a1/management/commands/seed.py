from django.core.management.base import BaseCommand
from a1.models import *

MODE_CLEAR = 'clear'

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('Starting...'))

        if options['mode'] == MODE_CLEAR:
            self.__clear_data()

    def __clear_data():
        pass

    def __create_authors():
        pass

    def __create_books():
        pass

    def __create_reviews():
        pass

    def __create_sales():
        pass