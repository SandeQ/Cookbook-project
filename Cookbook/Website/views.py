from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .forms import AddRecipe, EditRecipe, Register, Login, ChangePassword
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import time
# Create your views here.

class Startpage(View):
    def get(self,request):
        return render(request, "index.html")

class Registration(View):
    def get(self,request):
        form = Register()
        context = {'form': form}
        return render(request, 'register.html', context)
    def post(self,request):
        form = Register(request.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=login, email=email, password=password)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'error.html', status=2137)


class PasswordChange(LoginRequiredMixin, View):
    def get(self,request):
        form = PasswordChangeForm(request.user.password)
        context = {'form': form}
        return render(request, 'changepassword.html', context)
    def post(self,request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return HttpResponseRedirect("/")
        else:
            return render(request, 'error.html', status=2137)
class LoginUser(View):
    def get(self,request):
        form = Login()
        context = {'form': form}
        return render(request, 'login.html', context)
    def post(self,request):
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return render(request, 'error.html', status=2137)

class LogoutUser(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.is_authenticated():
            logout(request)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')



class RecipeAdd(LoginRequiredMixin,View):

    def get(self,request):
        form = AddRecipe()
        context= {'form': form}
        return render(request, 'addrecipe.html', context)

    def post(self,request):
        form = AddRecipe(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            ingredients = form.cleaned_data['ingredients']
            text = form.cleaned_data['text']
            prepare_time = form.cleaned_data['prepare_time']
            id = request.user.id
            Recipe.objects.create(Title=title, Ingredients = ingredients, Text = text, Preparation_Time = prepare_time, UserID = id)

            return HttpResponseRedirect("/showall")
        else:
            return render(request, 'error.html', status=2137)

class RecipeEdit(LoginRequiredMixin, View):

    def get(self,request, id):
        uid = request.user.id

        obj = Recipe.objects.get(pk=id)
        if obj.UserID == uid or request.user.is_superuser:
            editform = EditRecipe(instance=obj)
            context = {'form': editform}
            return render(request, 'editrecipe.html', context)
        else:
            return render(request,'403.html', status=403)


    def post(self,request, id):
        recipe = Recipe.objects.get(pk=id)
        edited_recipe = EditRecipe(request.POST,instance=recipe)
        edited_recipe.save()
        return HttpResponseRedirect("/")



    #nie działa, naprawić jutro

    #chuj gówno nie dziala edytowanie usuwanie kurwa chuj łeb mnie napierdala ide spac

class RecipeDelete(LoginRequiredMixin,View):
    def get(self,request,id):
        uid = request.user.id
        recipe = Recipe.objects.get(pk=id)
        if uid == recipe.UserID or request.user.is_superuser:
            recipe.delete()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseForbidden("403 BRAK UPRAWNIEŃ")

class ShowAll(View):
    def get(self,request):
        all_recipes = Recipe.objects.all()
        id = request.user.id
        context = {'all_recipes': all_recipes, 'id': id}
        return render (request,'showall.html', context)






class Dupa(View):
    def get(self,request):
        return render(request, "dupa.html")
#TODO
#1. dodawanie przepisu - weryfikacja czy konto jest aktywne
#2. zmienic w logowaniu template na osobny dla bledu logowania









































##################################################

# pk = request.GET.get('id', '')
"""def GetRecipeID(request):
    counter=0
    form = GetRecipeByID()
    context = {'form': form}

    if request.method == 'POST':
        form = GetRecipeByID(request.POST)
        id = form['recipeid'].value()

        obj = Recipe.objects.get(pk=id)
        editform = EditRecipe()
        context = {'form': editform}
        if editform.is_valid():
            return HttpResponse("OK")
        return HttpResponseRedirect("editrecipe/%i" % int(form['recipeid'].value()))
    return render (request, 'getrecipeid.html', context)"""


"""def Registration(request):
    form = Register()
    context = {'form': form}
    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=login, email=email, password=password)
            return HttpResponse("Zarejestrowano")

    return render(request, 'register.html', context)"""



"""def RecipeAdd(request):
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

    return render (request, 'addrecipe.html', context)"""

"""def DeleteRecipe(request):
    form = GetRecipeByID()
    context = {'form':form}

    if request.method == 'POST':
        form = GetRecipeByID(request.POST)
        id = form['recipeid'].value()
        recipe = Recipe.objects.get(pk=id)
        recipe.delete()

        return HttpResponse("Usunięto")
    return render(request, 'getrecipeid.html',context)"""

"""class PasswordChange(LoginRequiredMixin, View):
    def get(self,request):
        form = ChangePassword()
        context = {'form': form}
        return render(request, 'changepassword.html', context)
    def post(self,request):
        form = ChangePassword(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['newpassword']
            old_password = form.cleaned_data['oldpassword']
            user = authenticate(username=request.user.username,password=old_password)
            if user is not None:
                User.set_password(self,new_password)
                return HttpResponse("OK")
            else:
                return HttpResponse("Dupa")"""

##################################################