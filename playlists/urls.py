from django.urls import path,re_path
from .views import (
    MovieListView, 
    MovieDetailView, 
    TVShowListView, 
    FeaturedPlaylistListView,
    PlaylistDetailView,
    TVShowDetailView,
    TVShowSeasonDetailView,
    SearchView 
    )

urlpatterns = [
    # re_path(r'my-detail/(?P<id>\d+)/$',FeaturedPlaylistListView.as_view()),
    path('', FeaturedPlaylistListView.as_view()),\
    path('movies/<slug:slug>/', MovieDetailView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('media/<int:pk>/', PlaylistDetailView.as_view()),
    path('search/', SearchView.as_view()),
    path('shows/<slug:showSlug>/seasons/<slug:seasonSlug>/', TVShowSeasonDetailView.as_view()),
    path('shows/<slug:slug>/seasons/', TVShowDetailView.as_view()),
    path('shows/<slug:slug>/', TVShowDetailView.as_view()),
    path('shows/', TVShowListView.as_view()),
    # path('object-rate/', rate_object_view)
]