from django import forms
from .models import GroceryItem

class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name', 'quantity', 'category']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(GroceryItemForm, self).__init__(*args, **kwargs)
