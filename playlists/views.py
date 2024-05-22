from django.http import Http404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import Avg
from streamX.db.models import PublishStateOptions
from django.shortcuts import get_object_or_404

from .mixins import PlaylistMixin
from .models import Playlist, MovieProxy, TVShowProxy, TVShowSeasonProxy
from videos.models import Video

class SearchView(PlaylistMixin, ListView):
    template_name = 'playlists/search_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        query = self.request.GET.get("q")
        if query is not None:
            context['title'] = f"Searched for {query}"
        else:
            context['title'] = 'Perform a search'
        return context
    
    def get_queryset(self):
        query = self.request.GET.get("q") # request.GET = {}
        return Playlist.objects.all().movie_or_show().search(query=query)



class MovieListView(PlaylistMixin, ListView):
    queryset = MovieProxy.objects.all()
    context_object_name = 'movies'
    template_name = 'playlists/movie_list.html'
    title = "Movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_rated_movies = MovieProxy.objects.annotate(avg_rating=Avg('ratings__value')).order_by('-avg_rating')[:5]
        all_movies = MovieProxy.objects.all()
        context['top_movies'] = top_rated_movies
        context['movies'] = all_movies
        return context


class MovieDetailView(PlaylistMixin, DetailView):
    template_name = 'playlists/movieDetail.html'
    queryset = MovieProxy.objects.all()
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        video_id = movie.get_movie_id()
        if video_id:
            context['video'] = Video.objects.filter(video_id=video_id).first()
        return context

class PlaylistDetailView(PlaylistMixin, DetailView):
    template_name = 'playlists/playlist_detail.html'
    queryset = Playlist.objects.all()

class TVShowListView(PlaylistMixin, ListView):
    queryset = TVShowProxy.objects.all()
    context_object_name = 'shows'
    template_name = 'playlists/tvShow_list.html'
    title = "TV Shows"

class TVShowDetailView(PlaylistMixin, DetailView):
    template_name = 'playlists/tvshow_detail.html'
    queryset = TVShowProxy.objects.all()
    context_object_name = 'show'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video'] = self.object.video  # Add the video to the context
        context['seasons'] = self.object.seasons
        return context


class TVShowSeasonDetailView(PlaylistMixin, DetailView):
    template_name = 'playlists/season_detail.html'
    queryset = TVShowSeasonProxy.objects.all()
    context_object_name = 'season'


    def get_object(self):
        kwargs = self.kwargs
        show_slug = kwargs.get("showSlug")
        season_slug = kwargs.get("seasonSlug")
        now = timezone.now()
        try:
            obj = TVShowSeasonProxy.objects.get(
                state=PublishStateOptions.PUBLISH,
                publish_timestamp__lte=now,
                parent__slug__iexact=show_slug,
                slug__iexact=season_slug
            )
        except TVShowSeasonProxy.MultipleObjectsReturned:
            qs = TVShowSeasonProxy.objects.filter(
                parent__slug__iexact=show_slug,
                slug__iexact=season_slug
            ).published()
            obj = qs.first()
            # log this
        except:
            raise Http404
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        season = self.object
        videos = season.videos.all()
        context['video'] = self.object.video
        context['videos'] = videos
        return context


        # qs = self.get_queryset().filter(parent__slug__iexact=show_slug, slug__iexact=season_slug)
        # if not qs.count() == 1:
        #     raise Http404
        # return qs.first()

class TVShowSeasonEpisodeDetailView(DetailView):
    template_name = 'playlists/episode_detail.html'
    context_object_name = 'video'
    queryset = TVShowSeasonProxy.objects.all()

    def get_object(self):
        kwargs = self.kwargs
        show_slug = kwargs.get("showSlug")
        season_slug = kwargs.get("seasonSlug")
        video_slug = kwargs.get("slug")
        
        now = timezone.now()
        video = Video.objects.get(state=PublishStateOptions.PUBLISH,
                publish_timestamp__lte=now,
                slug__iexact=video_slug)
        
        return video

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = self.object
        return context

class FeaturedPlaylistListView(PlaylistMixin, ListView):
    template_name = 'playlists/featured_list.html'
    queryset = Playlist.objects.featured_playlists()
    title = "Featured"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = MovieProxy.objects.all()[:8]  # Add the video to the context
        context['shows'] = TVShowProxy.objects.all()[:8]
        top_rated_movies = MovieProxy.objects.annotate(avg_rating=Avg('ratings__value')).order_by('-avg_rating')[:5]
        context['top_movies'] = top_rated_movies

        latest_shows = TVShowProxy.objects.all().order_by('-timestamp')[:5]
        context['latest_shows'] = latest_shows
        return context