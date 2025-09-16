from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'movie/detail.html', {'post': post, 'comments': comments})

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['post', 'content', 'parent']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CommentReply(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'main_app/comment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        form.instance.parent_id = self.kwargs['comment_id']
        return super().form_valid(form)
    
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'description', 'image']

class PostDelete(DeleteView):
    model = Post
    success_url = '/movie/'

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
class Home(LoginView):
    template_name = 'home.html'

@login_required 

def movie(request):
    posts = Post.objects.all()
    return render(request, 'movie/movie.html', {'posts': posts})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   