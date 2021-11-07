from django.shortcuts import render, redirect
from .models import Recipe, Nutrient
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms.utils import ErrorList 
from django import forms

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import csv
from django.http import HttpResponse


# Create your views here.
# 레시피 목록
class RecipeList(ListView):
    model = Recipe
    ordering = '-pk'


# 레시피 상세
class RecipeDetail(DetailView):
    model = Recipe


# 레시피 삭제
class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipe/'
    context_object_name = 'recipe'


# 레시피 수정
class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'content']
    
    template_name = 'recipe/recipe_update_form.html'
    
    success_url = '/recipe/'

    def dispatch(self, request, *args, **kwargs):
        # 로그인 되어져있는지 + 로그인된 사용자와 글 작성자가 같은지
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(RecipeUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


# 대문 페이지
def index(request):
    return render(request, 'recipe/index.html')


#
def nutrient_list(request):
    return render(request, 'recipe/nutrient_list.html')


# 오늘의 식품 News
def todayNews(request):
    return render(request, 'recipe/todayNews.html')


# About 페이지(소개 페이지)
def about(request):
    return render(request, 'recipe/about.html')


# 로그인 페이지
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # 로그인에 성공하면
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        # 로그인에 실패하면
        else:
            return render(request, 'recipe/login.html', {'error': 'Please Try Again'})
    else:
        return render(request, 'recipe/login.html')


# 회원가입 페이지
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            )
            # 소셜로그인으로 가져온 정보를 다른 곳에 저장한다면 맨 뒤의 ModelBackend 부분을 수정
            #auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            auth.login(request, user)
            return redirect('/')
        else:  # 비밀번호 2개가 같지 않으면
            return render(request, 'recipe/signup.html')
    return render(request, 'recipe/signup.html')

    '''
    form = UserCreationForm
    return render(request, 'signup.html', {'form':form})
    '''


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('/')


# 내가 쓴 게시글 확인 페이지
def mypost(request):
    return render(request, 'recipe/mypost.html')


# 레시피 등록 페이지
def writeRecipe(request):
    return render(request, 'recipe/writeRecipe.html')




# csv를 model로 바꿔주기
def add_nutrients(request):
    path = '/workspace/1918_ShareYourRecipe/foodNutrientsdb.csv'
    csvfile = open(path)
    reader = csv.reader(csvfile)
    print("--------read success>> ", reader)
    list = []
    i = 0
    for row in reader:
        if i > 59257 : break;
        list.append(Nutrient(fname=row[0],
                             cl1=row[1],
                             cl2=row[2],
                             svs=row[3],
                             kcal=row[4],
                             protein_g=row[5],
                             fat_g=row[6],
                             carbo_g=row[7],
                             sugar_g=row[8],
                             calc_mg=row[9],
                             pota_mg=row[10],
                             salt_mg=row[11]))
        i += 1
    Nutrient.objects.bulk_create(list)
    return HttpResponse('foodNutrientsdb saved')



def nutrient_list(request):
    q=request.GET.get('q','')
    if (len(q)>=1):
        qs=Nutrient.objects.filter(fname__icontains=q)
    return render(request, 'recipe/nutrient_list.html',
                  {
                    'nutrient_list':qs,
                    'q':q
                })


