from django.urls import path
from .views import GroceryItemListView, GroceryItemCreateView, GroceryItemUpdateView, GroceryItemDeleteView, GroceryItemDetailView

urlpatterns = [
    path('', GroceryItemListView.as_view(), name='home'),
    path('create/', GroceryItemCreateView.as_view(), name='grocery_item_create'),
    path('update/<int:pk>/', GroceryItemUpdateView.as_view(), name='grocery_item_update'),
    path('delete/<int:pk>/', GroceryItemDeleteView.as_view(), name='grocery_item_delete'),
    path('detail/<int:pk>/', GroceryItemDetailView.as_view(), name='grocery_item_detail'),
]
