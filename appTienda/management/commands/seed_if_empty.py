from django.core.management.base import BaseCommand
from django.core.management import call_command
from appTienda.models import Producto

class Command(BaseCommand):
    help = "Carga seed_appTienda.json sólo si la BD está vacía"

    def handle(self, *args, **options):
        if Producto.objects.exists():
            self.stdout.write(self.style.SUCCESS("Seed: ya hay productos, no se carga."))
            return

        call_command("loaddata", "seed_appTienda.json")
        self.stdout.write(self.style.SUCCESS("Seed cargado OK."))
