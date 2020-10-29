from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class CheckoutForm(forms.Form):
    amount = forms.IntegerField()

    class Meta():
        fields = ['amount']
