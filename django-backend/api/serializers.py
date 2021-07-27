from rest_framework.serializers import ModelSerializer
from postapp.models import GhostPost

class PostSerializer(ModelSerializer):
  class Meta:
    model = GhostPost
    fields = '__all__'