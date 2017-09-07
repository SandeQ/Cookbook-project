"""Cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Website.views import Startpage
from Website.views import Dupa
from Website.views import RecipeAdd
from Website.views import ShowAll
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', Startpage),
    url(r'^dupa', Dupa),
    url(r'^addrecipe', RecipeAdd),
    url(r'^showall', ShowAll)
]
