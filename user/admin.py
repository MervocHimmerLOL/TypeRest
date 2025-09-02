from django.contrib import admin
from .models import User

# Ну а тут регистрируем модель юзеров
admin.site.register(User)
