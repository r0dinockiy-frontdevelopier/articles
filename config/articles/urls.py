from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleUpdateView,  ArticleDeleteView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles', ArticleListView.as_view(), name='article_list'),
    path('articles/create', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),

]
