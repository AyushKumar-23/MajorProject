from videos.models import Video
from playlists.models import Playlist

# Create your tests here.
video_a = Video.objects.create(title="My Title",video_id="1")

obj_a = Playlist.objects.create(title="This is my title",video=video_a)