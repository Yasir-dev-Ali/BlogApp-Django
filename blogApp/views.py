from   django.shortcuts import  render


def Post(Request):
    return render(Request,"main/post.html")


# PostListView
# PostDetailView
# PostCreateView
# PostUpdateView
# PostDeleteView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .model import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'main/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'main/post_form.html'
    fields = ['title', 'content']
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'main/post_detail.html'
    fields = ['title', 'content']
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    





    

