import os

from django.core.management.base import BaseCommand
from tenant_schemas.utils import get_tenant_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        columns = ('schema_name', 'domain_url')
        tenant_model = get_tenant_model()
        tenants = tenant_model.objects.exclude(schema_name='public').values_list(*columns)

        for tenant in tenants:
            os.system("./manage.py tenant_command populate_users_do_not_run_manually --schema={}".format(tenant[0]))
