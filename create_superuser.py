from django.contrib.auth import get_user_model
import os
import django

"""
    Criar um super usuário automaticamente no deploy.
"""

# Configurar as variáveis de ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cursodjango.settings')
django.setup()

User = get_user_model()

# Configurações do superusuário
# SUPERUSER_USERNAME = os.getenv('SUPERUSER_USERNAME', 'admin')
SUPERUSER_EMAIL = os.getenv('SUPERUSER_EMAIL', 'admin@example.com')
SUPERUSER_PASSWORD = os.getenv('SUPERUSER_PASSWORD', 'adminpassword')

# if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
if not User.objects.filter(email=SUPERUSER_EMAIL).exists():
    User.objects.create_superuser(
        # username=SUPERUSER_USERNAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD,
    )
    print("Superusuário criado com sucesso!")
else:
    print("O superusuário já existe.")
