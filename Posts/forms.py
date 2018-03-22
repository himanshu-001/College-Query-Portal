from django import forms
from Posts.models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('title', 'body')