from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_grocery_item, name='create_grocery_item'),
    path('edit/<int:item_id>/', views.edit_grocery_item, name='edit_grocery_item'),
    path('delete/<int:item_id>/', views.delete_grocery_item, name='delete_grocery_item'),
    path('view/<int:item_id>/', views.grocery_item_detail, name='grocery_item_detail'),
]