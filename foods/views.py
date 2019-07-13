from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Food
from django.utils import timezone

# Create your views here.
def home(request):
    foods = Food.objects
    return render(request, 'foods/home.html', {'foods': foods})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['restaurant'] and request.POST['headline'] and request.POST['description'] and request.FILES['image']:
            food = Food()
            food.name = request.POST['name']
            food.restaurant = request.POST['restaurant']
            food.headline = request.POST['headline']
            food.description = request.POST['description']
            food.image = request.FILES['image']
            food.pub_date = timezone.datetime.now()
            food.likes = 1
            food.hunter = request.user
            food.save()
            return redirect('/foods/' + str(food.id))

        else:
            return render(request, 'foods/create.html', {'error': 'All fields must be valid'})
    else:
        return render(request, 'foods/create.html')

def detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'foods/detail.html', {'food': food})

@login_required(login_url="/accounts/signup")
def likes(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        food.likes += 1
        food.save()
        return redirect('/foods/' + str(food.id))
