from django.core.management.base import BaseCommand
from clients.models import Client
from multitenantproject.settings import URL_DOMAIN


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Public Schema
        domain_url = "{}".format(URL_DOMAIN)
        if not Client.objects.filter(domain_url=domain_url).exists():
            Client.objects.create(
                domain_url=domain_url,
                schema_name="public",
                name='local',
                email_contact='public@gmail.com'
            )
            print("Created organization with domain URL: {}".format(domain_url))

        domain_url = "python.{}".format(URL_DOMAIN)
        if not Client.objects.filter(domain_url=domain_url).exists():
            Client.objects.create(
                domain_url=domain_url,
                schema_name="python",
                name='python',
                email_contact='python@gmail.com'
            )
            print("Created organization with domain URL: {}".format(domain_url))

        domain_url = "reactjs.{}".format(URL_DOMAIN)
        if not Client.objects.filter(domain_url=domain_url).exists():
            Client.objects.create(
                domain_url=domain_url,
                schema_name="reactjs",
                name='reactjs',
                email_contact='reactjs@gmail.com'
            )
            print("Created organization with domain URL: {}".format(domain_url))

        domain_url = "testmodels.{}".format(URL_DOMAIN)
        if not Client.objects.filter(domain_url=domain_url).exists():
            Client.objects.create(
                domain_url=domain_url,
                schema_name="testmodels",
                name='testmodels',
                email_contact='testmodels@gmail.com'
            )
            print("Created organization with domain URL: {}".format(domain_url))
