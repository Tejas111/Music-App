from django.db import models
from django.contrib.auth.models import Permission,User
# Create your models here.
class album(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    artist=models.CharField(max_length=250)
    title=models.CharField(max_length=150)
    genre= models.CharField(max_length=250)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.title + '-' + self.artist

class song(models.Model):
    Album = models.ForeignKey(album,on_delete=models.CASCADE)
    filetype=models.CharField(max_length=250)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.song_title