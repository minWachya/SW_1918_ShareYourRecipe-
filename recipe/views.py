from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView


# Create your views here.
class RecipeList(ListView):
    model = Recipe
    ordering = '-pk'


class RecipeDetail(DetailView):
    model = Recipe


def index(request):
    return render(request, 'recipe/index.html')


def Search(request):
    return render(request, 'recipe/Search.html')


def todayNews(request):
    return render(request, 'recipe/todayNews.html')


def board(request):
    return render(request, 'recipe/board.html')


def about(request):
    return render(request, 'recipe/about.html')


def login(request):
    return render(request, 'recipe/login.html')


def mypost(request):
    return render(request, 'recipe/mypost.html')


def writeRecipe(request):
    return render(request, 'recipe/writeRecipe.html')
