from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import Q

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

#Search functionality
def search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query) | Movie.objects.filter(genre__icontains=query)
    else:
        movies = Movie.objects.none()  # Return an empty queryset if no query is provided
    movie_count = movies.count()

    context = {
        'movies': movies,
        'query': query,
        'movie_count':movie_count,
    }
    return render(request, 'movies/search.html', context)