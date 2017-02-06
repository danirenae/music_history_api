from django.db import models
from . import artist_model

class Genre(models.Model):
  """
  The Genre table maintains the information related to a musical genre
  """
  genre_label = models.CharField(max_length=200)
  artist = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Genres'

  def __str__(self):
    return '{}'.format(self.genre_label)