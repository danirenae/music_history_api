"""music_history URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from music_history_api.views import *
from rest_framework import routers

router = routers. DefaultRouter()
router.register(r'user', user_view.UserViewSet)
router.register(r'artists', artist_view.ArtistViewSet)
router.register(r'albums', album_view.AlbumViewSet)
router.register(r'genres', genre_view.GenreViewSet)
router.register(r'songs', song_view.SongViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



