from django.shortcuts import render, redirect
from .models import GroceryItem, Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import GroceryItemSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

class GroceryItemViewSet(viewsets.ModelViewSet):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer
    permission_classes = [AllowAny] 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny] 

# @login_required
def home(request):
    if request.user.is_authenticated:
        grocery_items = GroceryItem.objects.filter(user=request.user)
    else:
        grocery_items = []
    
    categories = Category.objects.all()
    
    context = {
        'grocery_items': grocery_items,
        'categories': categories,
    }
    return render(request, 'home.html', context)


@login_required
@api_view(['POST'])
def create_grocery_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)

        GroceryItem.objects.create(
            name=name,
            quantity=quantity,
            user=request.user,
            category=category
        )

        return HttpResponseRedirect(reverse('home'))

@login_required
@api_view(['PUT'])
def edit_grocery_item(request, item_id):
    grocery_item = GroceryItem.objects.get(id=item_id, user=request.user)

    if request.method == 'POST':
        grocery_item.name = request.POST['name']
        grocery_item.quantity = request.POST['quantity']
        category_id = request.POST['category']
        grocery_item.category = Category.objects.get(id=category_id)
        grocery_item.save()

        return redirect('home')


@login_required
@api_view(['DELETE'])
def delete_grocery_item(request, item_id):
    grocery_item = GroceryItem.objects.get(id=item_id, user=request.user)

    if request.method == 'POST':
        grocery_item.delete()
        return redirect('home')

@login_required
@api_view(['GET'])
def grocery_item_detail(request, item_id):
    grocery_item = GroceryItem.objects.get(id=item_id, user=request.user)
    return render(request, 'grocery_item_detail.html', {'grocery_item': grocery_item})

