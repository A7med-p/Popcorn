from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
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
    return render(request, 'movie/detail.html', {'post': post})

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'image']
    
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'description', 'image']

class PostDelete(DeleteView):
    model = Post
    success_url = '/movie/'
    
class Home(LoginView):
    template_name = 'home.html'

@login_required 

def movie(request):
    posts = Post.objects.filter(user=request.user)
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
   