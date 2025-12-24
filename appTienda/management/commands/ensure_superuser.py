import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Crea o actualiza un superusuario (sin interacción)."

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@admin.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin")

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email, "is_staff": True, "is_superuser": True},
        )

        # Asegura permisos y email
        user.email = email
        user.is_staff = True
        user.is_superuser = True

        # Importante: SIEMPRE deja la clave como la env var (para que nunca te quedes fuera)
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Superusuario '{username}' creado y password seteada."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superusuario '{username}' actualizado (password reseteada)."))
