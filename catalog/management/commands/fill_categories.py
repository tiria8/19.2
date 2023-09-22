from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Спальня', 'description': 'Мебель для спальни'},
            {'name': 'Детская', 'description': 'Мебель для детской'},
            {'name': 'Ванная', 'description': 'Мебель для ванной комнаты'},
            {'name': 'Гостиная', 'description': 'Мебель для гостиной'},
            {'name': 'Кухня', 'description': 'Мебель для кухни'},
            {'name': 'Прихожая', 'description': 'Мебель для прихожей'}
        ]

        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(
                Category(**category)
            )
        Category.objects.bulk_create(categories_for_create)
