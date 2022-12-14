from django.urls import path
from .views import(
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView
)
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from django.conf import settings


urlpatterns = [
    path('',ArticleListView.as_view() , name="article_list"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),

]