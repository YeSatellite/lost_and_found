from django.db import models

from customauth.models import MyUser


class LostPost(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    text = models.TextField(max_length=1000, default='')
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
