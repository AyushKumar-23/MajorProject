from django.contrib import admin
from .models import VideoAllProxy, VideoPublishedProxy

# Register your models here.
class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['id','title','video_id','state','is_published','get_playlist_ids']
    search_fields = ['title']
    list_filter = ['state','active']
    readonly_fields = ['id','is_published',"publish_timestamp",]

    class Meta:
        model = VideoAllProxy

    # def published(self,obj,*args,**kwargs):
    #     return obj.active

admin.site.register(VideoAllProxy,VideoAllAdmin)

class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title','video_id']
    search_fields = ['title']
    # list_filter
    class Meta:
        model = VideoPublishedProxy
    
    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)
    
admin.site.register(VideoPublishedProxy,VideoPublishedProxyAdmin)