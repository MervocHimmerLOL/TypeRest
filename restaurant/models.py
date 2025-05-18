from django.db import models


# Модель блюда. Имя, описание, необязательная картинка, цена, и категория
class Dish(models.Model):
    name = models.CharField("Название", max_length=40)
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2, default=0.00)
    category = models.CharField("Категория", max_length=40)

    # Отображение в админке - имя
    def __str__(self):
        return self.name
