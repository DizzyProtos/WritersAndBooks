from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'creates test data in DB'

    def handle(self, *args, **options):
        call_command('migrate')
        call_command('loaddata', 'writers.json')
        call_command('loaddata', 'books.json')
