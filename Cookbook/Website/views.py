from django.shortcuts import render
from django import views
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddRecipe
from .models import Recipe
# Create your views here.

def Startpage(request):
    return render(request, "index.html")
def Dupa(request):
    return render(request, "dupa.html")
def RecipeAdd(request):
    form = AddRecipe()
    context = {'form': form}

    if request.method == 'POST':
        form = AddRecipe(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            ingredients = form.cleaned_data['ingredients']
            text = form.cleaned_data['text']
            prepare_time = form.cleaned_data['prepare_time']
            Recipe.objects.create(Title=title, Ingredients = ingredients, Text = text, Preparation_Time = prepare_time)

            return HttpResponse("ok")
        else:
            return HttpResponse("Coś się, coś się popsuło")

    return render (request, 'addrecipe.html', context)
def ShowAll(request):
    all_recipes = Recipe.objects.all()
    context = {'all_recipes': all_recipes}
    return render (request,'showall.html', context)
