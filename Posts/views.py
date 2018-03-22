from django.shortcuts import get_object_or_404

from accounts.models import Profile
from Comments.forms import CommentForm
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from Posts.models import Post
from Comments.models import Comment


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    extra_context = {"prof": Profile.objects.all()}


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'post_detail.html'

class PostDetail(FormMixin, DetailView):
    template_name = 'post_detail.html'
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = self.object
        comment.save()
        # want to save post instance here.
        return super(PostDetail, self).form_valid(form)
