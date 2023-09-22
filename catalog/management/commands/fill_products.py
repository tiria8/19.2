from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'name': 'Диван', 'description': 'Диван двуспальный', 'category': Category.objects.get(pk=4), 'price': 25000},
            {'name': 'Стол', 'description': 'Стол угловой', 'category': Category.objects.get(pk=5), 'price': 7000},
            {'name': 'Стул кухонный', 'category': Category.objects.get(pk=5), 'price': 1000},
            {'name': 'Кровать детская', 'category': Category.objects.get(pk=2), 'price': 10000},
            {'name': 'Вешалка', 'category': Category.objects.get(pk=6), 'price': 2000},
            {'name': 'Раковина', 'category': Category.objects.get(pk=3), 'price': 4500}
        ]

        products_for_create = []
        for product in products_list:
            products_for_create.append(
                Product(**product)
            )
        Product.objects.bulk_create(products_for_create)
