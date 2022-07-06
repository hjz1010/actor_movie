from django.urls import path

from movies_v2.views import ActorsView, MoviesView

urlpatterns = [
    path('/actors', ActorsView.as_view()),
    path('/movies', MoviesView.as_view())
]
