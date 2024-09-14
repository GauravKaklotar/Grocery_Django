from django.contrib import admin
from .models import Category, GroceryItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'category', 'user')
    list_filter = ('category', 'user')