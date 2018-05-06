from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from Posts.models import Post
from django.utils import timezone
# from markdown import markdown
# from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = RichTextUploadingField(verbose_name='Leave a Comment :')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comments

    # def get_comments_as_markdown(self):
    #     return mark_safe(markdown(self.comments, safe_mode='escape'))