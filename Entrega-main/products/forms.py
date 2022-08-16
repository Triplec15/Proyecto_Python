from django import forms
from products.models import Products
from products.models import Contacto
from products.models import Categoria

class Product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class Contacto_form(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        
class Categoria_form(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
