from django.urls import path
from . import views

urlpatterns = [
    # 클래스 호출
    path('', views.index),
    path('Search/', views.Search),
    path('todayNews/', views.todayNews),
    path('board/', views.board),
    path('about/', views.about),
    path('login/', views.login),
    path('post/', views.RecipeList.as_view())
    # path('<int:pk>/', views.PostDetail.as_view()),
]