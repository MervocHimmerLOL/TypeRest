from django.contrib import admin
from .models import Order

# Тут мы зарегистрировали нашу модель заказа
admin.site.register(Order)
