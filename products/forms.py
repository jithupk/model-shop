from django import forms
from .models import product_list
class ModelForm(forms.ModelForm):
    class Meta:
        model = product_list
        fields = ['name', 'description', 'price', 'image']
        
