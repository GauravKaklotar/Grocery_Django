from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from .models import GroceryItem, Category
from .forms import GroceryItemForm

class GroceryItemListView(ListView):
    model = GroceryItem
    context_object_name = 'grocery_items'
    template_name = 'home.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return GroceryItem.objects.filter(user=self.request.user)
        return GroceryItem.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Pass categories to the template
        return context


class GroceryItemCreateView(BSModalCreateView):
    template_name = 'grocery_item_create_modal.html'
    form_class = GroceryItemForm
    success_message = 'Grocery item created successfully!'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroceryItemUpdateView(BSModalUpdateView):
    model = GroceryItem
    template_name = 'grocery_item_update_modal.html'
    form_class = GroceryItemForm
    success_message = 'Grocery item updated successfully!'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return GroceryItem.objects.filter(user=self.request.user)


class GroceryItemDeleteView(BSModalDeleteView):
    model = GroceryItem
    template_name = 'grocery_item_delete_modal.html'
    success_message = 'Grocery item deleted successfully!'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return GroceryItem.objects.filter(user=self.request.user)
    
    
class GroceryItemDetailView(DetailView):
    model = GroceryItem
    template_name = 'grocery_item_detail.html'
    context_object_name = 'grocery_item'

    def get_queryset(self):
        return GroceryItem.objects.filter(user=self.request.user)