from django.core.management.base import BaseCommand
from main.models import DRFTest

class Command(BaseCommand):
    def populate(self):
        obj = DRFTest(name="Test Object 1", description="This is a test DRF Object 1.")
        obj.save()
        obj = DRFTest(name="Test Object 2", description="This is a test DRF Object 2.")
        obj.save()



    def handle(self, *args, **options):
        # self._create_types()
        # self._create_suits()
        # self.__create_ranks()
         self.populate()