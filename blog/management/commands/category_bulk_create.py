from django.core.management import BaseCommand

from blog.models import Category


class Command(BaseCommand):
    help = "created for bulk operation"

    def handle(self, *args, **options):
        category_list = ["Python", "Java", "Araba", "Javascript",
                         "Linux", "Css", "Html", "React", "Spor", "Devops"]
        for category_name in category_list:
            Category.objects.get_or_create(name=category_name)
