from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from movies.models import Actor, Movie, Actor_Movie

# Create your views here.


class ActorsView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            middles = Actor_Movie.objects.filter(actor=actor.id)
            movie_list = []
            for middle in middles:
                movie = Movie.objects.get(id=middle.movie_id)
                movie_list.append(movie.title)
            results.append({
                "이름": actor.first_name,
                "성": actor.last_name,
                "출연한 영화들": movie_list
            })
        return JsonResponse({"results": results}, status=200)


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            middles = Actor_Movie.objects.filter(movie_id=movie.id)
            actor_list = []
            for middle in middles:
                actor = Actor.objects.get(id=middle.actor_id)
                actor_list.append(actor.first_name)
            results.append({
                "영화 제목": movie.title,
                "상영 시간": movie.running_time,
                "출연 배우들": actor_list
            })
        return JsonResponse({"results": results}, status=200)
