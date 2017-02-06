from django.db import models


class Artist(models.Model):
  """
  The Artist table maintains the information related to individual artists
  """
  artist_name = models.CharField(max_length=200)
  year_established = models.DateField()

  class Meta:
    verbose_name_plural = 'Artists'

  def __str__(self):
    return '{}'.format(self.artist_name)