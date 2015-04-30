from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(default='', blank=True, max_length=128)
    content = models.TextField()
    category = models.ForeignKey('Category', blank=True, null=True)

