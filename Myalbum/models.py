from django.db import models

# Create your models here.
class Myalbum(models.Model):

    thumbnail = models.ImageField(upload_to='album/photo/')
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
