from django.apps import AppConfig


# Конфиг аппы
class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'

    def ready(self):
        import restaurant.cart_session
