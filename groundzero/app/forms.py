from django import forms
from .models import Formulario, Producto


class FormularioForm(forms.ModelForm):
    
    class Meta:
        model = Formulario
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__' 

        widgets ={
            "fecha_creacion":forms.SelectDateWidget()
        }