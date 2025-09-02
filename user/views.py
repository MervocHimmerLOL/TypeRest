from django.shortcuts import render, redirect
from django.contrib import messages
from order.models import Order
from .form import CustomUserCreationForm


# Вьюшка регистрации
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


# Вьшка профиля, где мы показываем заказы пользователю
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user/profile.html', {
        'orders': orders
    })
