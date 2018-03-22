from Comments.models import Comment
from django import forms

from Posts.models import Post


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add Comments Here...'}))

    class Meta:
        model = Comment
        fields = ['text']
