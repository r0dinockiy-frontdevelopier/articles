from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('article_list')

    
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')

