from Comments.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    # comments = forms.CharField(label='Leave a Comment :', widget=forms.Textarea, required=False)

    class Meta:
        model = Comment
        fields = ['comments']
