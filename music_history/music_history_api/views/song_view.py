from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class SongViewSet(viewsets.ModelViewSet):
    """
    This creates the Song view
    """
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer