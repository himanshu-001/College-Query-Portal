from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from Posts.models import Post
from django.utils import timezone


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Leave a Comment :')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text