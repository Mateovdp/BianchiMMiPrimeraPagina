from django import forms

class FormularioCreacionCliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    documento = forms.IntegerField()
    localidad = forms.CharField(max_length=20)