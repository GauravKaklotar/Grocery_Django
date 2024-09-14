from rest_framework import serializers
from .models import GroceryItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class GroceryItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = GroceryItem
        fields = '__all__'
