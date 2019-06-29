from rest_framework import serializers

from .model import Profile


class ProfileSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True, style={'input_type': 'password'})

  class Meta:
    model = Profile
    fields = (
      "id",
      "username",
      "password",
    )
