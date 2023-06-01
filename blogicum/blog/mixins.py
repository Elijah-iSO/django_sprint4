from django.core.exceptions import PermissionDenied

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from . models import Comment, Post
from . forms import CommentForm


class AuthorCheckMixin:

    def dispatch(self, request, *args, **kwargs):
        self.posts = get_object_or_404(Post, pk=kwargs['pk'])
        if self.posts.author != request.user:
            return redirect('blog:post_detail', self.kwargs['pk'])
        else:
            return super().dispatch(request, *args, **kwargs)


class CommentMixin:
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'
    success_url = reverse_lazy('blog:index')

    def get_object(self, queryset=None):
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        return get_object_or_404(
            Comment, id=comment_id, post_id=post_id, author=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail',
                            kwargs={'pk': self.kwargs.get('post_id')})
