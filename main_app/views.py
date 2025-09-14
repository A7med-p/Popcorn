from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

class Post:
    def __init__(self, title, image, description):
        self.title = title
        self.image = image
        self.description = description
        
posts = [
    Post('MOVIE1', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4EIuDx-tBVTI70CWerfKz41XOl5JoTmqo_A&s', 'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into something much, much more.'),
    Post('MOVIE2', 'https://m.media-amazon.com/images/I/51oD6C1bGDL._AC_SY445_.jpg', 'A ticking-time-bomb insomniac and a slippery soap salesman channel'),
]
def movie(request):
    return render(request, 'movie/movie.html', {'posts': posts})
