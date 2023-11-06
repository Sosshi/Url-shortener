from django.db import models
from django.contrib.auth.models import User


class ShortnerModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    slug = models.SlugField(max_length=9)
    count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.slug
