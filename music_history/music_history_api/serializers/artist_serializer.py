from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Artist Model
    """
    class Meta:
        model = artist_model.Artist
        fields = '__all__'