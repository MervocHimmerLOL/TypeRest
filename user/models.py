from django.contrib.auth.models import AbstractUser
from django.db import models


# Модель наследуем от стандартной, и добавляем туда телефон
class User(AbstractUser):
    phone = models.CharField(max_length=40, blank=True)
