from django.conf.urls import include, url
from rest_framework import routers, urlpatterns
from .views import GhostPostView

router = routers.DefaultRouter()

router.register('post', GhostPostView)

urlpatterns = [
  url(r'^api/', include(router.urls))
]