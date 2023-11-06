from django.db import models


class ShortnerModel(models.Model):
    original_url = models.URLField()
    slug = models.SlugField(max_length=9)

    def __str__(self) -> str:
        return self.slug
