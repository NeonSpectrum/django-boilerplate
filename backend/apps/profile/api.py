from rest_framework.viewsets import ModelViewSet

from .model import Profile
from .serializer import ProfileSerializer


class ProfileViewSet(ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
