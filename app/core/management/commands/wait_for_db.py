"""custom command to wait for database server ready"""

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from time import sleep


class Command(BaseCommand):
    """command to wait for database ready"""

    def handle(self, *args, **kwargs):
        """command handler"""
        db_up = False
        self.stdout.write('waiting for database...')

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.ERROR(
                    'Database unavailable . Waiting one second...'
                ))
                sleep(1)
            
        self.stdout.write(self.style.SUCCESS('Database available'))