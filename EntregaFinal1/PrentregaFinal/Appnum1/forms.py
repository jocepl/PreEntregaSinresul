from django import forms

class ColabFormulario(forms.Form):

        legajo = forms.IntegerField()
        nombre = forms.CharField(max_length=40)
        apellido = forms.CharField(max_length=40)
        edad = forms.IntegerField()
        categoria_venta = forms.CharField(max_length=60)


class BuyerFormulario(forms.Form):

        nombre = forms.CharField(max_length=40)
        apellido = forms.CharField(max_length=40)
        email = forms.EmailField()
        direccion = forms.CharField(max_length=70)
        tlf = forms.IntegerField()


class SellerFormulario(forms.Form):

        nombre = forms.CharField(max_length=40)
        categoria = forms.CharField(max_length=50)
        email = forms.EmailField()