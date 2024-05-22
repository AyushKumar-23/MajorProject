from django.urls import path
from .views import (
    MovieListView, 
    MovieDetailView, 
    TVShowListView, 
    FeaturedPlaylistListView,
    PlaylistDetailView,
    TVShowDetailView,
    TVShowSeasonDetailView,
    SearchView,
    TVShowSeasonEpisodeDetailView
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # re_path(r'my-detail/(?P<id>\d+)/$',FeaturedPlaylistListView.as_view()),
    path('', FeaturedPlaylistListView.as_view()),
    path('movies/<slug:slug>/', login_required(MovieDetailView.as_view(),login_url='/user/login/?next=/user/login/'), name='movie-detail'),
    path('movies/', login_required(MovieListView.as_view(),login_url='/user/login/?next=/user/login/') ,name='movie-list'),
    path('media/<int:pk>/', login_required(PlaylistDetailView.as_view(),login_url='/user/login/?next=/user/login/')),
    path('search/', login_required(SearchView.as_view(),login_url='/user/login/?next=/user/login/')),
    path('shows/<slug:showSlug>/seasons/<slug:seasonSlug>/<slug:slug>/', 
         login_required(TVShowSeasonEpisodeDetailView.as_view(), login_url='/user/login/?next=/user/login/'), 
         name='episode_detail'),
    path('shows/<slug:showSlug>/seasons/<slug:seasonSlug>/', login_required(TVShowSeasonDetailView.as_view(),login_url='/user/login/?next=/user/login/') ,name='season_detail'),
    path('shows/<slug:slug>/seasons/', login_required(TVShowDetailView.as_view(),login_url='/user/login/?next=/user/login/')),
    path('shows/<slug:slug>/', login_required(TVShowDetailView.as_view(),login_url='/user/login/?next=/user/login/'), name='show-detail'),
    path('shows/', login_required(TVShowListView.as_view(),login_url='/user/login/?next=/user/login/'), name='show-list'),
    # path('object-rate/', rate_object_view)
]