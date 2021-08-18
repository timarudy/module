from .models import Item, Purchase, User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='юзернейм:', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='пароль:', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='пароль:', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
          model = User
          fields = ['username', 'password1', 'password2']

class ItemCheckForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'in_stock']

class ItemPurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['amount']