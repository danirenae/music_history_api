from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Song Model
    """
    class Meta:
        model = models.Song
        fields = '__all__'