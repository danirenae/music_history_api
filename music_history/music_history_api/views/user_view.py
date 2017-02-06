from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    This creates the User view
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer