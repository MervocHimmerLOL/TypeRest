from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Dish
from order.models import Order, OrderItems


# Вьюшки ресторана - самая нагруженная часть кода. С одной стороны, логику корзинки можно было бы перенести в order
# А с другой - как будто бы и тут хорошо сидит

# Стартовая страница. Дом. Показывает блюда по фильтру, а если вы и залогиненны - даже даст добавить их в корзину
def home(request):
    category_filter = request.GET.get('category')

    if category_filter:
        dishes = Dish.objects.filter(category=category_filter)
    else:
        dishes = Dish.objects.all()

    categories = Dish.objects.values_list('category', flat=True).distinct()

    if request.method == 'POST':
        dish_id = str(request.POST.get('dish_id'))
        cart = request.session.get('cart', {})

        if dish_id in cart:
            cart[dish_id] += 1
        else:
            cart[dish_id] = 1

        request.session['cart'] = cart

    return render(request, 'home/index.html', {
        'dishes': dishes,
        'categories': categories,
        'current_category': category_filter
    })


# Просмотр корзинки - только для своих
@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for dish_id, quantity in cart.items():
        dish = Dish.objects.get(id=int(dish_id))
        subtotal = dish.price * quantity
        total += subtotal
        cart_items.append({
            'dish': dish,
            'quantity': quantity,
            'subtotal': subtotal
        })
    return render(request, 'restaurant/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# Создание заказа - только для своих. Можно будет добавить настоящую оплату
@login_required
def place_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('view_cart')

        order = Order.objects.create(user=request.user)
        total = 0

        for dish_id, quantity in cart.items():
            dish = Dish.objects.get(id=int(dish_id))
            price = dish.price
            OrderItems.objects.create(
                order=order,
                dish=dish,
                quantity=quantity,
                price_at_order=price
            )
            total += price * quantity

        order.total = total
        order.save()
        request.session['cart'] = {}
        return render(request, 'restaurant/order_success.html', {'order': order})

    return redirect('home')


# Плюсик в корзинке
@login_required
def add_to_cart(request, dish_id):
    cart = request.session.get('cart', {})
    cart[str(dish_id)] = cart.get(str(dish_id), 0) + 1
    request.session['cart'] = cart
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)


# Минусик в корзинке
@login_required
def remove_from_cart(request, dish_id):
    cart = request.session.get('cart', {})
    if str(dish_id) in cart:
        cart[str(dish_id)] -= 1
        if cart[str(dish_id)] <= 0:
            del cart[str(dish_id)]
    request.session['cart'] = cart
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)


# Удаление пункта из корзинки
@login_required
def delete_from_cart(request, dish_id):
    cart = request.session.get('cart', {})
    cart.pop(str(dish_id), None)
    request.session['cart'] = cart
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)


# Тотальная отчистка. Где? В корзинке
@login_required
def clear_cart(request):
    request.session['cart'] = {}
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)
