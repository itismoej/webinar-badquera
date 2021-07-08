from datetime import timedelta

from django.db import models
from django.utils import timezone


def _60_days_from_now():
    return timezone.now() + timedelta(days=60)


class College(models.Model):
    price = models.IntegerField(default=60_000)
    is_open = models.BooleanField(default=True)
    open_at = models.DateTimeField(default=timezone.now)
    close_at = models.DateTimeField(default=_60_days_from_now)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)


class Chapter(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    required_chapter = models.ForeignKey("Chapter", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=True)
    order = models.IntegerField(default=0)


class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=None, null=True)
    text = models.TextField()
