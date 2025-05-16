from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField("Название",max_length=40)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2, default=0.00)
    category = models.CharField("Категория", max_length=40)

    def __str__(self):
        return self.name