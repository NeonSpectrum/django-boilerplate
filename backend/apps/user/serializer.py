from rest_framework import serializers
from .model import User

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True, style={'input_type': 'password'})

  class Meta:
    model = User
    fields = (
      "id",
      "username",
      "password",
    )
