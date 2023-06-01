from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .forms import CommentForm, PostForm
from .mixins import AuthorCheckMixin, CommentMixin
from .models import Category, Post, User
from .paginator import paginate_default_value, get_page_obj


class IndexListView(ListView):
    model = Post
    queryset = Post.objects.prefetch_related(
        'comments').select_related(
        'author').filter(pub_date__lt=timezone.now(),
                         is_published=True, category__is_published=True,
                         ).annotate(comment_count=Count('comments'))
    template_name = 'blog/index.html'
    ordering = '-pub_date'
    paginate_by = paginate_default_value


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.all(),
        is_published=True,
        slug=category_slug)
    post_list = category.posts.all(
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date').annotate(
        comment_count=Count('comments')
    )
    page_number = request.GET.get('page')
    page_obj = get_page_obj(post_list, page_number, paginate_default_value)
    context = {'page_obj': page_obj,
               'category': category}
    return render(request, 'blog/category.html', context)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = (
            self.object.comments.select_related('author')
        )
        return context


def user_profile(request, username):
    profile = get_object_or_404(User, username=username)
    queryset = Post.objects.select_related('author').filter(
        author__username=username,).order_by(
        '-pub_date').annotate(comment_count=Count('comments'))
    page_number = request.GET.get('page')
    page_obj = get_page_obj(queryset, page_number, paginate_default_value)
    context = {'profile': profile, 'page_obj': page_obj, }
    return render(request, 'blog/profile.html', context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'blog/user.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse(
            'blog:profile',
            kwargs={'username': self.request.user.username})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    def get_success_url(self):
        return reverse_lazy(
            'blog:profile',
            kwargs={'username': self.request.user}
        )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, AuthorCheckMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail',
                            kwargs={'pk': self.posts.pk})


class PostDeleteView(LoginRequiredMixin, AuthorCheckMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse_lazy('blog:index')


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('blog:post_detail', pk=pk)


class CommentUpdateView(LoginRequiredMixin, CommentMixin, UpdateView):
    pass


class CommentDeleteView(LoginRequiredMixin, CommentMixin, DeleteView):
    pass
