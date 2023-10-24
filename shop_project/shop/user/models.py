from django.contrib.auth.models import AbstractUser
from django.db import models

from services.validators import validate_username


class AuthUser(AbstractUser):
    username = models.CharField(max_length=50, blank=False, unique=True, validators=[validate_username])

    class Meta:
        db_table = 'Users'
