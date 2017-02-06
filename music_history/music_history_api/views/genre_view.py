from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class GenreViewSet(viewsets.ModelViewSet):
    """
    This creates the Genre view
    """
    queryset = genre_model.Genre.objects.all()
    serializer_class = genre_serializer.GenreSerializer