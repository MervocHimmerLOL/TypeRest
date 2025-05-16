from django.shortcuts import render
from .models import Dish
# Create your views here.
def home(request):
    dishes = Dish.objects.all()
    return render(request, 'home/index.html', {'dishes' : dishes})