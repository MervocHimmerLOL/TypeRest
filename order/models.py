from django.db import models
from django.contrib.auth import get_user_model
from restaurant.models import Dish

# Модель нашего заказа
# т.к. юзер у нас кастомный, то его сначала надо получить
User = get_user_model()


# Сам класс модели, модель у нас состоит из: заказавшего юзера, блюд, статуса заказа, даты создания и общей стоимости.
class Order(models.Model):
    STATUS_CHOICES = [
        ('preparing', 'Готовится'),
        ('delivering', 'Доставляется'),
        ('completed', 'Завершен')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    dishes = models.ManyToManyField(Dish, through='OrderItems', verbose_name='Блюда')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Готовится')
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField('Общая стоимость', max_digits=10, decimal_places=2, default=0.00)

    # Человекочитаемость в админку
    def __str__(self):
        return f'Заказ #{self.pk} от {self.user.username}'


# Подмодель, нужна для красивого отображения заказа в виде
# пицца - 2 н-ное количество рублей, так же отвечает за сумму позиции
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Блюдо')
    quantity = models.PositiveIntegerField('Количество', default=1)
    price_at_order = models.DecimalField('Цена', max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.price_at_order:
            self.price_at_order = self.dish.price
        super().save(*args, **kwargs)
