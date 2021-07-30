from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
import subprocess

class Command(BaseCommand):
  def handle(self, *args, **options):
    new_secret_key = get_random_secret_key()

    with open('./djangobackend/.env', 'w') as f:
      f.write(f"SECRET_KEY='{new_secret_key}'")
    with open('../.gitignore', 'a') as f:
      f.write('.env')

    subprocess.run(['git', 'rm', '-r', '--cached', 'djangobackend/.env'])
    subprocess.run(['python', 'manage.py', 'migrate'])