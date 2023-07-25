from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):

    image = ImageField()

    text = models.CharField(max_length=140, blank=False, null=False)


    def __str__(self):
        return self.text
