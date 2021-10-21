from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 클래스 호출
    path('', views.index),
    path('Search/', views.Search),
    path('todayNews/', views.todayNews),
    path('about/', views.about),
    path('login/', views.login),
    # 레시피 올리기 post -> writeRecipe
    # path('post/', views.RecipeList.as_view()),
    path('writeRecipe/', views.writeRecipe),
    # 레시피 보기 board -> recipe_list
    # path('board/', views.board),
    path('recipe/', views.RecipeList.as_view()),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view()),
    path('mypost/', views.mypost),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)