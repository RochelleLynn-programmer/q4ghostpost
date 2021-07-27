from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    boast = models.BooleanField()
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submitted = models.DateTimeField(default= timezone.now)


    def __str__(self):
      return self.content