from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Genre Model
    """
    class Meta:
        model = genre_model.Genre
        fields = '__all__'