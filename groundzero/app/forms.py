from django import forms
from .models import Formulario, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioForm(forms.ModelForm):
    
    class Meta:
        model = Formulario
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    nombre =forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False)
    precio = forms.IntegerField(min_value=1)

    class Meta:
        model = Producto
        fields = '__all__' 

        widgets ={
            "fecha_creacion":forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = 'username', "first_name", "last_name", "email", "password1", "password2"