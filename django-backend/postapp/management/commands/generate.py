from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
from postapp.models import GhostPost
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

    GhostPost.objects.bulk_create([
      GhostPost(boast=True, content="Integer semper eros sed malesuada finibus. Curabitur ac dolor at tellus rhoncus feugiat. Sed sed.", upvotes=10, downvotes=5),
      GhostPost(boast=True, content="Vivamus at ante eget lorem tempor porta in eu nibh. Ut ullamcorper, eros ac ultrices.", upvotes=15, downvotes=7),
      GhostPost(boast=True, content="Sed tempor elementum dictum. Nam dapibus dapibus neque, ut luctus sem ultricies ac. Ut dictum..", upvotes=3, downvotes=15),
      GhostPost(boast=True, content="Nunc blandit velit et lobortis sollicitudin. Integer volutpat hendrerit mi vel interdum. Nulla vitae eleifend.", upvotes=25, downvotes=0),
      GhostPost(boast=True, content="In tincidunt tempor erat, at tincidunt nibh euismod placerat. Nulla rhoncus aliquam justo eget aliquet.", upvotes=11, downvotes=2),
      GhostPost(boast=False, content="Quisque eu pretium nulla. Maecenas volutpat ullamcorper lorem non malesuada. Maecenas dictum ligula felis, id.", upvotes=1, downvotes=5),
      GhostPost(boast=False, content="Sed odio velit, tempor vel viverra ac, convallis at nibh. Aliquam erat volutpat. Curabitur ac.", upvotes=18, downvotes=12),
      GhostPost(boast=False, content="Maecenas consectetur nisi ac venenatis tristique. Phasellus quam tortor, malesuada ut pharetra a, pellentesque vel.", upvotes=4, downvotes=17),
      GhostPost(boast=False, content="Duis vitae maximus leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris et ex.", upvotes=100, downvotes=20),
      GhostPost(boast=False, content="Donec a odio eget urna fermentum gravida quis non nisl. Aenean tempus congue elit. Praesent.", upvotes=0, downvotes=50),
    ])