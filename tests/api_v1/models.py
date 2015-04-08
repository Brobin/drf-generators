from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(default='', blank=True, max_length=128)
    content = models.TextField()
