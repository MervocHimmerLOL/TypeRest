from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Тут у нас кастомные(не совсем) формочки регистрации и входа
# Получаем кастомную модель пользователя
User = get_user_model()


# Локализация входа
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Имя пользователя'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Введите имя пользователя'),
        })
    )

    password = forms.CharField(
        label=_('Пароль'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Введите пароль'),
        })
    )


# Локализация регистрации
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=_('Имя пользователя'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Введите имя пользователя')
        })
    )
    email = forms.CharField(
        label=_('Электронная почта'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Введите электронную почту')
        })
    )

    password1 = forms.CharField(
        label=_('Пароль'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Введите пароль'),
        }),
        help_text=_('Минимум 8 символов, '
                    'не должен быть похож на '
                    'имя пользователя, '
                    'верхний и нижний регистр')
    )

    password2 = forms.CharField(
        label=_('Подтверждение пароля'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Подтвердите пароль'),
        }),
    )

    # Говорим, какие поля включать в форму регистрации
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
