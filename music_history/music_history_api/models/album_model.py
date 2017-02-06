from django.db import models
from . import artist_model

class Album(models.Model):
  """
  The Album table maintains the information related to an album
  """
  album_title = models.CharField(max_length=200)
  release_date = models.DateField()
  album_duration = models.IntegerField(default=0)
  artist = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Albums'

  def __str__(self):
    return '{} {}'.format(self.album_title, self.artist)