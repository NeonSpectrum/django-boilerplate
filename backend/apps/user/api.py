from rest_framework.viewsets import ModelViewSet
from .model import User
from .serializer import UserSerializer

class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
