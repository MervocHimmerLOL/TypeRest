from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


# отчистка корзинки в каждый заход/выход из аккаунта
@receiver(user_logged_in)
def clear_cart_on_login(sender, user, request, **kwargs):
    request.session['cart'] = {}
