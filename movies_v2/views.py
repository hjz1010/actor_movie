from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from movies_v2.models import Actor, Movie
# Create your views here.


class ActorsView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            movies = actor.movies.all()
            movie_list = []
            for movie in movies:
                movie_list.append(movie.title)
            results.append({
                "이름": actor.first_name,
                "성": actor.last_name,
                "출연작": movie_list
            })
        return JsonResponse({'results': results}, status=200)


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actors = movie.actors.all()
            actor_list = []
            for actor in actors:
                actor_list.append(actor.first_name)
            results.append({
                "제목": movie.title,
                "상영시간": movie.running_time,
                "출연 배우": actor_list
            })
        return JsonResponse({'results': results}, status=200)
