from rest_framework.routers import DefaultRouter

from apps.user.api import UserViewSet


class Router(DefaultRouter):
  def __init__(self):
    super(DefaultRouter, self).__init__()
    self.trailing_slash = '/?'


router = Router()
router.register(r'users', UserViewSet)
