from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F

from .serializers import PostSerializer

from postapp import models

class GhostPostView(ModelViewSet):
  serializer_class = PostSerializer
  queryset = models.GhostPost.objects.all().order_by('-submitted')

  @action(detail=False, methods=['get'])
  def highest_rated(self, request):
    posts = models.GhostPost.objects.all().order_by(F('downvotes')-F('upvotes'))
    serializer = self.get_serializer(posts, many=True)
    return Response(serializer.data)

  @action(detail=False, methods=['get'])
  def roasts(self, request):
    posts = models.GhostPost.objects.filter(boast=False).order_by('-submitted')
    serializer = self.get_serializer(posts, many=True)
    return Response(serializer.data)

  @action(detail=False, methods=['get'])
  def boasts(self, request):
    posts = models.GhostPost.objects.filter(boast=True).order_by('-submitted')
    serializer = self.get_serializer(posts, many=True)
    return Response(serializer.data)

  @action(detail=True, methods=['post'])
  def upvote(self, request, pk=None):
    post = self.get_object()
    post.upvotes += 1
    post.save()
    serializer = self.get_serializer(post, many=False)
    return Response(serializer.data)

  @action(detail=True, methods=['post'])
  def downvote(self, request, pk=None):
    post = self.get_object()
    post.downvotes += 1
    post.save()
    serializer = self.get_serializer(post, many=False)
    return Response(serializer.data)

