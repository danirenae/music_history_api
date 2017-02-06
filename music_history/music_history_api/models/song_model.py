from django.db import models
from django.contrib.auth.models import User
from . import artist_model, album_model, genre_model

class Song(models.Model):
  """
  The Album table maintains the information related to an individual song
  """
  song_title = models.CharField(max_length=200)
  song_duration = models.IntegerField(default=0)
  artist_name = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)
  album = models.ForeignKey(album_model.Album, on_delete=models.CASCADE)
  genre = models.ForeignKey(genre_model.Genre, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Songs'

  def __str__(self):
    return '{} {} {}'.format(self.song_title, self.artist_name, self.album)
