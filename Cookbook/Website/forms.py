from django import forms

class AddRecipe(forms.Form):
    title = forms.CharField(label='Podaj nazwę przepisu, krótszą niż 100 znaków', max_length=100)
    ingredients = forms.CharField(label="Składniki(max 300 znaków): ", max_length=300)
    text = forms.CharField(label="Tu wpisz przepis: ")
    prepare_time = forms.IntegerField(label="Podaj czas przyrządzania w minutach")
