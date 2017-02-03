from django.contrib.auth.models import User
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


class Genre(models.Model):
  """
  The Genre table maintains the information related to a musical genre
  """
  genre_label = models.CharField(max_length=200)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Genres'

  def __str__(self):
    return '{}'.format(self.genre_label)


class Album(models.Model):
  """
  The Album table maintains the information related to an album
  """
  album_title = models.CharField(max_length=200)
  release_date = models.DateField()
  album_duration = models.IntegerField(default=0)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Albums'

  def __str__(self):
    return '{} {}'.format(self.album_title, self.artist)


class Song(models.Model):
  """
  The Album table maintains the information related to an individual song
  """
  song_title = models.CharField(max_length=200)
  song_duration = models.IntegerField(default=0)
  artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Songs'

  def __str__(self):
    return '{} {} {}'.format(self.song_title, self.artist_name, self.album)



