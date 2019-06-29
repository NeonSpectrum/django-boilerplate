from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
  user = models.OneToOneField(
    get_user_model(),
    on_delete=models.CASCADE,
  )
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  class Meta:
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
