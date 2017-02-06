from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class GenreViewSet(viewsets.ModelViewSet):
    """
    This creates the Genre view
    """
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer