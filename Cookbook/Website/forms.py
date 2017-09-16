from django import forms
from .models import Recipe
from django.forms import ModelForm

class AddRecipe(forms.Form):
    title = forms.CharField(label='Podaj nazwę przepisu, krótszą niż 100 znaków', max_length=100)
    ingredients = forms.CharField(label="Składniki(max 300 znaków): ", max_length=300)
    text = forms.CharField(label="Sposób przyrządzenia: ",widget=forms.Textarea)
    prepare_time = forms.IntegerField(label="Podaj czas przyrządzania w minutach")
class GetRecipeByID(forms.Form):
    recipeid = forms.IntegerField(label="Podaj id przepisu który chcesz edytować")
class EditRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['Title','Ingredients','Text','Preparation_Time']
    """title = forms.CharField(label='Podaj nazwę przepisu, krótszą niż 100 znaków', max_length=100)
    ingredients = forms.CharField(label="Składniki(max 300 znaków): ", max_length=300)
    text = forms.CharField(label="Sposób przyrządzenia: ")
    prepare_time = forms.IntegerField(label="Podaj czas przyrządzania w minutach")"""
class Login(forms.Form):
    username = forms.CharField(label='Podaj swój login: ')
    password = forms.CharField(label='Podaj hasło', widget=forms.PasswordInput)
class Register(forms.Form):
    login = forms.CharField(label='Podaj swoją nazwę użytkownika: ')
    email = forms.CharField(label='Podaj swój adres e-mail w celu odzyskiwania hasła')
    password1 = forms.CharField(label='Podaj swoje hasło: ', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Podaj hasło ponownie w celu weryfikacji',widget=forms.PasswordInput)
class ChangePassword(forms.Form):
    oldpassword = forms.CharField(label='Podaj swoje hasło: ', widget=forms.PasswordInput)
    newpassword = forms.CharField(label='Podaj swoje hasło: ', widget=forms.PasswordInput)
