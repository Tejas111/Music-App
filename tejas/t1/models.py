from django.db import models

# Create your models here.
class album(models.Model):
    title=models.CharField(max_length=150)
    genre= models.CharField(max_length=250)
    def __str__(self):
        return self.title
class song(models.Model):
    Album = models.ForeignKey(album,on_delete=models.CASCADE)
    filetype=models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.filetype