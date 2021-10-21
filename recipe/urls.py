from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 클래스 호출
    path('', views.index),
    path('Search/', views.Search),
    path('todayNews/', views.todayNews),
    path('board/', views.board),
    path('about/', views.about),
    path('login/', views.login),
    path('post/', views.RecipeList.as_view()),
    path('post/<int:pk>/', views.RecipeDetail.as_view()),
    path('mypost/', views.mypost),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)