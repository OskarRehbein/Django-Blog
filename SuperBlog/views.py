from django.shortcuts import render 
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Post 
from .forms import FormPost, EditPost


#def home(request):
#   return render(request, 'home.html', {})


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewPostView(CreateView):
    model = Post
    form_class = FormPost
    template_name = 'new_post.html'
            #fields = '__all__' ## The easy way that it don't understand right now, so i followed the other that just integrates the fields manually
            #fields = ('title', 'title_tag', 'body') #Now test tag shouldn't appear in the new post page, adn since i havent added user, i left author out

class NewEditView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    #fields = ['title','title_tag', 'body']
    form_class = EditPost
