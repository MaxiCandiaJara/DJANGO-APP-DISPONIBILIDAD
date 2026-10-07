#!/usr/bin/env bash
# Script de build para Render
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# Crear superusuario automáticamente si las variables están definidas
python manage.py shell -c "
from django.contrib.auth.models import User
import os

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', '')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f'Superusuario {username} creado exitosamente!')
    else:
        print(f'Superusuario {username} ya existe.')
else:
    print('Variables DJANGO_SUPERUSER_USERNAME/PASSWORD no definidas, saltando creacion de superusuario.')
"
