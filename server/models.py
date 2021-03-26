from django.db import models


class BlogCategory(models.Model):

    name = models.CharField(max_length=256, verbose_name='Name Category')
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name
