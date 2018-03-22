from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return "%s (%s)" % (self.title, self.user.first_name)

    def get_absolute_url(self):
        return reverse("post_detail", args=str(self.id))
