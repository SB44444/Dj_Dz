from django.core.management.base import BaseCommand, CommandParser
from dz_app2.models import Order, User
# from datetime import datetime


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='User id to order')

    def handle(self, *args, **kwargs):
        pk = kwargs['id']
        customer = User.objects.filter(pk=pk).first()
        order = Order(customer=customer, products='Pizza_Cheese', total_price=499.00)
        order.save()
        self.stdout.write(f'{order}')
