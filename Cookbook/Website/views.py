from django.shortcuts import render
from django import views
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddRecipe, GetRecipeByID, EditRecipe
from .models import Recipe
# Create your views here.
def DeleteRecipe(request):
    form = GetRecipeByID()
    context = {'form':form}

    if request.method == 'POST':
        form = GetRecipeByID(request.POST)
        id = form['recipeid'].value()
        recipe = Recipe.objects.get(pk=id)
        recipe.delete()

        return HttpResponse("Usunięto")
    return render(request, 'getrecipeid.html',context)
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
def GetRecipeID(request):
    counter=0
    form = GetRecipeByID()
    context = {'form': form}

    if request.method == 'POST':
        form = GetRecipeByID(request.POST)
        id = form['recipeid'].value()

        """obj = Recipe.objects.get(pk=id)
        editform = EditRecipe()
        context = {'form': editform}
        if editform.is_valid():
            return HttpResponse("OK")"""
        return HttpResponseRedirect("editrecipe/%i" % int(form['recipeid'].value()))
    return render (request, 'getrecipeid.html', context)
def RecipeEdit(request,id):
    if request.method == 'POST':
        obj = Recipe.objects.get(pk=id)
        editform = EditRecipe()
        context = {'form': editform}

        return render(request, 'editrecipe.html', context)
    #nie działa, naprawić jutro

    #chuj gówno nie dziala edytowanie usuwanie kurwa chuj łeb mnie napierdala ide spac

