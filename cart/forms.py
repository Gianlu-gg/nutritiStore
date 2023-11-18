from django import forms

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(max_length=100)