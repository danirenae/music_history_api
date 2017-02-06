from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Explixitly creates a User serializer
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'is_superuser', 'last_login',)