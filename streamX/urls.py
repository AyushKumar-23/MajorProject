from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from ratings.views import rate_object_view

admin.site.site_header = "StreamX Login Portal"
admin.site.site_title = "StreamX Admin Portal"
admin.site.index_title = "Welcome to StreamX Admin Portal | You can manage the content from this portal"

urlpatterns = [
   re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),

    path("user/",include("user.urls")),
    path("user/",include("django.contrib.auth.urls")),

    path("category/",include('categories.urls')),
    path("categories/",include('categories.urls')),
    
    path('tags/',include('tags.urls')),

    path('object-rate/', rate_object_view),

    path("",include("playlists.urls")),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
# ]