from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Album Model
    """
    class Meta:
        model = album_model.Album
        fields = '__all__'