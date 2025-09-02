"""
URL configuration for type_rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views, authenticate
from user import views as user_views
from restaurant.views import home, view_cart, place_order, add_to_cart, remove_from_cart, delete_from_cart, clear_cart
from user.form import CustomLoginForm

# тут у нас харянтся url-ы + static для работы с фотками заказов
urlpatterns = [
                  path('', home, name='home'),
                  path('admin/', admin.site.urls),
                  path('login/', auth_views.LoginView.as_view(
                      template_name='user/login.html',
                      authentication_form=CustomLoginForm),
                       name='login'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
                  path('register/', user_views.register, name='register'),
                  path('profile/', user_views.profile, name='profile'),
                  path('cart/', view_cart, name='view_cart'),
                  path('place_order/', place_order, name='place_order'),
                  path('add/<int:dish_id>/', add_to_cart, name='add_to_cart'),
                  path('remove/<int:dish_id>/', remove_from_cart, name='remove_from_cart'),
                  path('delete/<int:dish_id>/', delete_from_cart, name='delete_from_cart'),
                  path('clear/', clear_cart, name='clear_cart')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
