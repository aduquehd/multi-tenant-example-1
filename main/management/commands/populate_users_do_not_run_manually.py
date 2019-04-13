from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = [
            {
                'username': "andresduque",
                'first_name': "Andres",
                'last_name': "Duque",
                'password': "123456",
            },
            {
                'username': "nelsonmartinez",
                'first_name': "Nelson",
                'last_name': "Martinez",
                'password': "123456",
            },
        ]

        for user in users:
            if not User.objects.filter(username=user['username']).exists():
                print(">>> User with username: '{}' created".format(user['username']))
                user_object = User(username=user['username'], first_name=user['first_name'],
                                   last_name=user['last_name'])
                user_object.set_password(user['password'])
                user_object.save()

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@gmail.com', '123456')
            print(">>> User with username: 'admin' created")
